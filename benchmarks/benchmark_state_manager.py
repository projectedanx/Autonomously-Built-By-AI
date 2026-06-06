import time
import os
import tempfile
from system_logic.state_manager import StateManager

def benchmark_mark_context_processed(num_iterations=1000):
    """Benchmarks the mark_context_processed method.

    Args:
        num_iterations (int): The number of iterations to run. Defaults to 1000.
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        manager = StateManager(workspace_root=tmpdir)

        filenames = [f"file_{i}.txt" for i in range(num_iterations)]

        start_time = time.perf_counter()
        for filename in filenames:
            manager.mark_context_processed(filename)
        end_time = time.perf_counter()

        duration = end_time - start_time
        print(f"Benchmark mark_context_processed with {num_iterations} iterations: {duration:.4f} seconds")
        print(f"Average time per call: {duration/num_iterations:.8f} seconds")


def benchmark_mark_context_processed_deferred(num_iterations=1000):
    """Benchmarks the mark_context_processed method with defer_save=True.

    Args:
        num_iterations (int): The number of iterations to run. Defaults to 1000.
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        manager = StateManager(workspace_root=tmpdir)

        filenames = [f"file_{i}.txt" for i in range(num_iterations)]

        start_time = time.perf_counter()
        for filename in filenames:
            manager.mark_context_processed(filename, defer_save=True)
        manager.save_state()
        end_time = time.perf_counter()

        duration = end_time - start_time
        print(f"Benchmark mark_context_processed_deferred with {num_iterations} iterations: {duration:.4f} seconds")
        print(f"Average time per call: {duration/num_iterations:.8f} seconds")
def benchmark_get_unprocessed_context(num_files=1000):
    """Benchmarks the get_unprocessed_context method.

    Args:
        num_files (int): The number of files to create in the inbox. Defaults to 1000.
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        manager = StateManager(workspace_root=tmpdir)

        # Create some files in inbox
        for i in range(num_files):
            with open(os.path.join(manager.inbox_dir, f"file_{i}.txt"), 'w') as f:
                f.write("test")

        # Mark half as processed
        for i in range(num_files // 2):
            manager.mark_context_processed(f"file_{i}.txt")

        start_time = time.perf_counter()
        # Call it multiple times to get a better measurement
        num_calls = 100
        for _ in range(num_calls):
            unprocessed = manager.get_unprocessed_context()
        end_time = time.perf_counter()

        duration = end_time - start_time
        print(f"Benchmark get_unprocessed_context with {num_files} files, {num_calls} calls: {duration:.4f} seconds")
        print(f"Average time per call: {duration/num_calls:.8f} seconds")

if __name__ == "__main__":
    print("Starting baseline benchmarks...")
    benchmark_mark_context_processed(1000)
    benchmark_mark_context_processed_deferred(1000)
    benchmark_get_unprocessed_context(1000)
