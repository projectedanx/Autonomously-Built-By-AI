import pytest
import numpy as np
from staged_advantage_estimation import StagedTrajectoryNode, TreeOPOGroup

def test_staged_trajectory_node_initialization():
    # [∇] Assuming basic initialization works as expected
    node = StagedTrajectoryNode("prefix_A")
    assert node.prefix_id == "prefix_A"
    assert node.parent_id is None
    assert node.total_rollouts == 0
    assert node.successful_rollouts == 0
    assert node.has_success_completion is False

def test_tree_opo_group_add_node():
    # [∇] Assuming basic node adding works
    group = TreeOPOGroup("group_1")
    group.add_node("prefix_A")
    group.add_node("prefix_B", "prefix_A")

    assert "prefix_A" in group.nodes
    assert "prefix_B" in group.nodes
    assert "prefix_B" in group.nodes["prefix_A"].children_ids

def test_tree_opo_group_register_sample():
    group = TreeOPOGroup("group_1")
    group.add_node("prefix_A")
    group.add_node("prefix_B", "prefix_A")

    idx = group.register_sample("prefix_B", 1.0)
    assert idx == 0
    assert group.nodes["prefix_B"].total_rollouts == 1
    assert group.nodes["prefix_B"].successful_rollouts == 1
    assert group.nodes["prefix_B"].has_success_completion is True

    # Check parent propagation
    assert group.nodes["prefix_A"].total_rollouts == 1
    assert group.nodes["prefix_A"].successful_rollouts == 1
    assert group.nodes["prefix_A"].has_success_completion is True

def test_heuristic_advantages():
    group = TreeOPOGroup("group_1")
    group.add_node("prefix_A")
    group.register_sample("prefix_A", 1.0)
    group.register_sample("prefix_A", 0.0)

    advantages = group.compute_heuristic_advantages(alpha=0.5)
    # V_E(p_A) = 1/2 = 0.5
    # raw_adv = [1.0 - 0.5*0.5, 0.0 - 0.5*0.5] = [0.75, -0.25]
    # mean = 0.25
    # final_adv = [0.5, -0.5]
    np.testing.assert_almost_equal(advantages, [0.5, -0.5])

def test_sae_qp_advantages():
    group = TreeOPOGroup("group_1")
    group.add_node("prefix_A")
    group.add_node("prefix_B", "prefix_A") # prefix_A is parent of prefix_B

    # To test C_pair constraint: a_A + margin <= a_B when r_A = 0, r_B = 1
    group.register_sample("prefix_A", 0.0) # idx 0
    group.register_sample("prefix_B", 1.0) # idx 1

    advantages = group.compute_sae_qp_advantages(margin=0.1)

    # sum(a) = 0 => a_A + a_B = 0 => a_A = -a_B
    # a_A + 0.1 <= a_B  => -a_B + 0.1 <= a_B => 0.1 <= 2a_B => a_B >= 0.05
    # Also tries to minimize ||a - r_0||^2

    assert np.isclose(np.sum(advantages), 0.0, atol=1e-5)
    assert advantages[0] + 0.1 <= advantages[1] + 1e-5
