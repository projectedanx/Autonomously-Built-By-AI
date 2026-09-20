import time
import numpy as np
import torch
from system_logic.staged_advantage_estimation import TreeOPOGroup

def run_benchmark():
    batch_sizes = [16, 32, 64, 128, 256, 512, 1024]

    print(f"{'Batch Size (N)':<15} | {'SLSQP Time (ms)':<15} | {'ADMM Time (ms)':<15} | {'Speedup':<10}")
    print("-" * 65)

    for N in batch_sizes:
        group = TreeOPOGroup(f'benchmark_N{N}')

        # Generate a balanced binary-like tree structure
        # prefix_id, reward
        samples = []
        for i in range(N):
            # Binary string representation for prefixes (e.g., '1', '10', '11')
            prefix_id = bin(i + 1)[2:]
            reward = float(np.random.rand())

            parent_id = prefix_id[:-1] if len(prefix_id) > 1 else None
            group.add_node(prefix_id, parent_id)
            group.register_sample(prefix_id, reward)


        # --- SLSQP Benchmark ---
        start_slsqp = time.perf_counter()
        # Fallback will kick in if SLSQP fails/timeouts, but we still measure
        try:
            adv_slsqp = group.compute_sae_qp_advantages(margin=0.01)
        except Exception as e:
            print(f"SLSQP failed at N={N}: {e}")
            adv_slsqp = None
        end_slsqp = time.perf_counter()
        time_slsqp_ms = (end_slsqp - start_slsqp) * 1000

        # --- ADMM Benchmark ---
        start_admm = time.perf_counter()
        adv_admm = group.compute_sae_admm_advantages(margin=0.01, device='cpu')
        end_admm = time.perf_counter()
        time_admm_ms = (end_admm - start_admm) * 1000

        speedup = time_slsqp_ms / time_admm_ms if time_admm_ms > 0 else float('inf')

        print(f"{N:<15} | {time_slsqp_ms:<15.2f} | {time_admm_ms:<15.2f} | {speedup:<10.2f}x")

if __name__ == '__main__':
    run_benchmark()
