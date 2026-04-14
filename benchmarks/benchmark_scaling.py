import time
import os
import json
import shutil
import tempfile
from system_logic.state_manager import StateManager

def benchmark_mark_context_processed(num_iterations=1000, initial_count=0):
    with tempfile.TemporaryDirectory() as tmpdir:
        manager = StateManager(workspace_root=tmpdir)

        if initial_count > 0:
            state = {"processed_context": [f"init_{i}.txt" for i in range(initial_count)]}
            manager._save_state(state)

        filenames = [f"file_{i}.txt" for i in range(num_iterations)]

        start_time = time.perf_counter()
        for filename in filenames:
            manager.mark_context_processed(filename)
        end_time = time.perf_counter()

        duration = end_time - start_time
        print(f"Benchmark mark_context_processed with {num_iterations} iterations (initial size {initial_count}): {duration:.4f} seconds")
        return duration

def benchmark_get_unprocessed_context(num_files=1000, initial_count=10000):
    with tempfile.TemporaryDirectory() as tmpdir:
        manager = StateManager(workspace_root=tmpdir)

        # Initial processed state
        state = {"processed_context": [f"init_{i}.txt" for i in range(initial_count)]}
        manager._save_state(state)

        # Create some files in inbox
        for i in range(num_files):
            with open(os.path.join(manager.inbox_dir, f"file_{i}.txt"), 'w') as f:
                f.write("test")

        start_time = time.perf_counter()
        # Call it multiple times to get a better measurement
        num_calls = 100
        for _ in range(num_calls):
            unprocessed = manager.get_unprocessed_context()
        end_time = time.perf_counter()

        duration = end_time - start_time
        print(f"Benchmark get_unprocessed_context with {num_files} files, {num_calls} calls (initial processed {initial_count}): {duration:.4f} seconds")
        return duration

def benchmark_reingest_artifacts(num_artifacts=100, initial_count=10000):
    with tempfile.TemporaryDirectory() as tmpdir:
        manager = StateManager(workspace_root=tmpdir)

        # Initial processed state
        state = {"processed_context": [f"init_{i}.txt" for i in range(initial_count)]}
        manager._save_state(state)

        # Create artifacts
        for i in range(num_artifacts):
            with open(os.path.join(manager.completed_dir, f"artifact_{i}.md"), 'w') as f:
                f.write("artifact content")

        start_time = time.perf_counter()
        # Call it
        manager.reingest_artifacts()
        end_time = time.perf_counter()

        duration = end_time - start_time
        print(f"Benchmark reingest_artifacts with {num_artifacts} artifacts (initial processed {initial_count}): {duration:.4f} seconds")
        return duration

if __name__ == "__main__":
    print("--- Scaling Benchmark (Baseline) ---")
    t1 = benchmark_mark_context_processed(100, initial_count=0)
    t2 = benchmark_mark_context_processed(100, initial_count=10000)

    t3 = benchmark_get_unprocessed_context(100, initial_count=10000)
    t4 = benchmark_reingest_artifacts(100, initial_count=10000)

    print("\nSummary:")
    print(f"mark_context_processed (100 calls, 0 initial): {t1:.4f}s")
    print(f"mark_context_processed (100 calls, 10000 initial): {t2:.4f}s")
    print(f"get_unprocessed_context (100 calls, 100 files, 10000 initial): {t3:.4f}s")
    print(f"reingest_artifacts (100 artifacts, 10000 initial): {t4:.4f}s")
