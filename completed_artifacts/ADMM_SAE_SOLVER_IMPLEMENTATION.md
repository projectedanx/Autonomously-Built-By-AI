# ADMM SAE Solver and Kinematic-Economic Coupling

## Overview
This artifact encapsulates the implementation of the Alternating Direction Method of Multipliers (ADMM) in PyTorch to solve the constrained convex Quadratic Program for Staged Advantage Estimation (SAE). This is paired with the implementation of Kinematic-Economic Coupling to penalize trajectories passing through exclusion zones.

## Core Implementations
1. `system_logic/admm_sae_solver.py`: Contains the `ADMMSolver` class that uses PyTorch tensor operations and Cholesky factorization for efficient constraints projection in $O(N^2)$ time.
2. `system_logic/staged_advantage_estimation.py`: Updated `TreeOPOGroup` to use `compute_sae_admm_advantages` as a drop-in replacement or alternative to the SLSQP baseline.
3. `system_logic/kinematic_constraints.py`: Contains physics simulation functions for calculating velocity ($v(m) = 1 + 5(\ln m / \ln 1000)^{1.5}$) and evaluating kinematic penalty margins against the solar singularity exclusion zone ($x_c, y_c = (50.0, 50.0), R = 10.0$).
4. `benchmarks/benchmark_admm_vs_slsqp.py`: Benchmarking script demonstrating the quadratic scaling superiority of ADMM over SLSQP at large batch sizes ($N \ge 512$).

## Epistemic Integrity
This implementation aligns with Pillar 2 of the Chrono-Kinematic Reversible AI Harness Specification, projecting raw rewards onto a zero-mean L2-ball while strictly enforcing prefix ordering DAG consistency constraints.
