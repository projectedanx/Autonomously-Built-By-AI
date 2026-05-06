import time
import os
import shutil
import tempfile
from system_logic.state_manager import StateManager

def benchmark_ensure_dirs(num_iterations=10000):
    with tempfile.TemporaryDirectory() as tmpdir:
        manager = StateManager(workspace_root=tmpdir)

        # We want to measure only the _ensure_dirs call.
        # Since it's called in __init__, we might need to call it manually for the benchmark.

        start_time = time.perf_counter()
        for _ in range(num_iterations):
            manager._ensure_dirs()
        end_time = time.perf_counter()

        duration = end_time - start_time
        print(f"Benchmark _ensure_dirs with {num_iterations} iterations: {duration:.6f} seconds")
        print(f"Average time per call: {duration/num_iterations:.10f} seconds")

if __name__ == "__main__":
    benchmark_ensure_dirs(10000)
