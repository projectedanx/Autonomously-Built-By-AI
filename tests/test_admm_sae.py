import pytest
import numpy as np
import torch
from system_logic.staged_advantage_estimation import TreeOPOGroup
from system_logic.admm_sae_solver import ADMMSolver

def test_admm_solver_basic_projection():
    """
    Test the basic convex projection constraints (mean zero, norm).
    """
    solver = ADMMSolver()

    # Unconstrained advantages
    r0 = torch.tensor([0.1, 0.5, 0.9, 0.2], dtype=torch.float32)
    r0 = r0 - torch.mean(r0)

    # No inequality constraints
    L = torch.zeros((0, 4), dtype=torch.float32)
    delta = torch.zeros(0, dtype=torch.float32)

    a = solver.solve(r0, L, delta)

    # Check mean zero constraint
    assert torch.abs(torch.sum(a)) < 1e-5

    # Check that a is close to r0 (since norm <= N is satisfied)
    assert torch.allclose(a, r0, atol=1e-5)

def test_admm_solver_inequality_constraints():
    """
    Test that ADMM strictly enforces L a + delta <= 0
    """
    solver = ADMMSolver()

    r0 = torch.tensor([1.0, 0.0, 0.5, -0.5], dtype=torch.float32)
    r0 = r0 - torch.mean(r0)

    # Force a_0 + margin <= a_1  => a_0 - a_1 + margin <= 0
    L = torch.zeros((1, 4), dtype=torch.float32)
    L[0, 0] = 1.0
    L[0, 1] = -1.0

    margin = 0.5
    delta = torch.tensor([margin], dtype=torch.float32)

    a = solver.solve(r0, L, delta)

    # Mean zero
    assert torch.abs(torch.sum(a)) < 1e-4

    # Inequality
    assert (a[0] - a[1] + margin).item() <= 1e-4

def test_tree_opo_group_admm_integration():
    """
    Test the full TreeOPOGroup wrapper for ADMM.
    """
    group = TreeOPOGroup('test_group')

    # Add nodes: root has child A and child B
    group.add_node('root')
    group.add_node('root_A', 'root')
    group.add_node('root_B', 'root')

    group.register_sample('root', 0.2)
    group.register_sample('root_A', 0.9)
    group.register_sample('root_B', 0.1)

    adv = group.compute_sae_admm_advantages(margin=0.1)

    assert adv.shape == (3,)
    assert np.abs(np.sum(adv)) < 1e-4
