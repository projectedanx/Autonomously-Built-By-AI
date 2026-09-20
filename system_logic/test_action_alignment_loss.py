import pytest
import torch
from system_logic.action_alignment_loss import ActionAlignmentLoss

def test_action_alignment_loss_nash_trap():
    """
    Test the Rock, Paper, Scissors 'Nash Trap' edge case.
    """
    # Payoff matrix: R, P, S
    payoff_matrix = torch.tensor([
        [0.0, -1.0, 1.0],
        [1.0, 0.0, -1.0],
        [-1.0, 1.0, 0.0]
    ])

    # Exact best response
    loss_fn = ActionAlignmentLoss(payoff_matrix=payoff_matrix, use_smooth=False)

    # Opponent plays Rock (index 0) with 100% confidence
    # Logits [10.0, -10.0, -10.0] gives probability ~[1.0, 0.0, 0.0]
    predicted_opponent_logits = torch.tensor([[10.0, -10.0, -10.0]])

    # Agent plays Nash [1/3, 1/3, 1/3]
    # Logits [0.0, 0.0, 0.0] gives probability [1/3, 1/3, 1/3]
    agent_logits = torch.tensor([[0.0, 0.0, 0.0]])

    loss = loss_fn(agent_logits, predicted_opponent_logits)

    # The expected regret should be exactly 1.0, as derived in the chain-of-thought proof.
    assert torch.isclose(loss, torch.tensor(1.0), atol=1e-4), f"Expected loss ~1.0, got {loss.item()}"

def test_action_alignment_loss_optimal():
    """
    Test that playing the optimal counter-strategy results in 0 loss.
    """
    payoff_matrix = torch.tensor([
        [0.0, -1.0, 1.0],
        [1.0, 0.0, -1.0],
        [-1.0, 1.0, 0.0]
    ])

    loss_fn = ActionAlignmentLoss(payoff_matrix=payoff_matrix, use_smooth=False)

    # Opponent plays Rock
    predicted_opponent_logits = torch.tensor([[10.0, -10.0, -10.0]])

    # Agent plays Paper (index 1) with 100% confidence
    agent_logits = torch.tensor([[-10.0, 10.0, -10.0]])

    loss = loss_fn(agent_logits, predicted_opponent_logits)

    # The expected regret should be 0.0
    assert torch.isclose(loss, torch.tensor(0.0), atol=1e-4), f"Expected loss ~0.0, got {loss.item()}"

def test_action_alignment_loss_smooth():
    """
    Test smooth best response approximation.
    """
    payoff_matrix = torch.tensor([
        [0.0, -1.0, 1.0],
        [1.0, 0.0, -1.0],
        [-1.0, 1.0, 0.0]
    ])

    loss_fn = ActionAlignmentLoss(payoff_matrix=payoff_matrix, use_smooth=True, temperature=0.1)

    predicted_opponent_logits = torch.tensor([[10.0, -10.0, -10.0]])
    agent_logits = torch.tensor([[0.0, 0.0, 0.0]])

    loss = loss_fn(agent_logits, predicted_opponent_logits)

    # Since it's a smooth maximum, the max value will be slightly higher than 1.0
    # Thus the regret should be slightly higher than 1.0
    assert loss.item() > 1.0, f"Expected smooth loss > 1.0, got {loss.item()}"

def test_action_alignment_loss_batching():
    """
    Test that the loss correctly computes the mean over a batch.
    """
    payoff_matrix = torch.tensor([
        [0.0, -1.0, 1.0],
        [1.0, 0.0, -1.0],
        [-1.0, 1.0, 0.0]
    ])

    loss_fn = ActionAlignmentLoss(payoff_matrix=payoff_matrix, use_smooth=False)

    predicted_opponent_logits = torch.tensor([
        [10.0, -10.0, -10.0], # Rock
        [-10.0, 10.0, -10.0], # Paper
    ])

    agent_logits = torch.tensor([
        [0.0, 0.0, 0.0], # Nash (Loss 1.0)
        [-10.0, -10.0, 10.0], # Optimal (Scissors vs Paper) (Loss 0.0)
    ])

    loss = loss_fn(agent_logits, predicted_opponent_logits)

    # Batch mean should be (1.0 + 0.0) / 2 = 0.5
    assert torch.isclose(loss, torch.tensor(0.5), atol=1e-4), f"Expected loss ~0.5, got {loss.item()}"
