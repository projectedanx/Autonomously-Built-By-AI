#!/usr/bin/env python3
"""
================================================================================
           QUANTUM-COGNITIVE EPISTEMIC WORKBENCH (QCEW)
                  PIPELINE ORCHESTRATOR & LAUNCHER
================================================================================
File: qed_pipeline_launcher.py
Description: This script orchestrates the concurrent execution of the QED
             Simulation Runner and the QED Interactive Review Terminal. It
             manages background sub-processes, directs real-time telemetry logs,
             and mounts the interactive command shell in a unified runtime.
================================================================================
"""

import os
import sys
import time
import subprocess
import threading

def run_simulation(stop_event):
    """Runs the simulation runner in a loop to generate telemetry."""
    print("[ORCHESTRATOR] Spawning background simulation thread...")
    try:
        # Run the simulation runner script
        proc = subprocess.Popen(
            [sys.executable, "/workspace/scratch/qed_simulation_runner.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        while proc.poll() is None:
            if stop_event.is_set():
                proc.terminate()
                break
            line = proc.stdout.readline()
            if line:
                # Stream simulation logs in a subtle gray to highlight background process
                print(f"\033[90m[SIM-ENGINE] {line.strip()}\033[0m")
            time.sleep(0.1)
            
        stdout, stderr = proc.communicate()
        if proc.returncode == 0:
            print("\n[ORCHESTRATOR] Background simulation completed successfully and populated qed_experience.db.")
        else:
            print(f"\n[ORCHESTRATOR] Background simulation exited with code {proc.returncode}.")
            if stderr:
                print(f"\033[91m[SIM-ERR] {stderr}\033[0m")
    except Exception as e:
        print(f"[ORCHESTRATOR] Failed to execute simulation: {e}")

def main():
    print("\033[1m================================================================================")
    print("           QUANTUM-COGNITIVE EPISTEMIC WORKBENCH (QCEW) ORCHESTRATOR            ")
    print("================================================================================\033[0m")
    
    stop_event = threading.Event()
    sim_thread = threading.Thread(target=run_simulation, args=(stop_event,), daemon=True)
    sim_thread.start()
    
    # Allow some time for database generation
    print("[ORCHESTRATOR] Warming up database environment...")
    time.sleep(2)
    
    print("\n[ORCHESTRATOR] Launching Interactive Review Terminal...\n")
    try:
        # Launch the interactive review terminal
        args = [sys.executable, "/workspace/scratch/qed_review_terminal.py"]
        if "--non-interactive" in sys.argv:
            args.append("--non-interactive")
            
        subprocess.run(args, check=True)
    except KeyboardInterrupt:
        print("\n[ORCHESTRATOR] Intercepted shutdown signal. Cleaning up background tasks...")
    finally:
        stop_event.set()
        sim_thread.join(timeout=3)
        print("[ORCHESTRATOR] Shutdown sequence complete. Epistemic alignment preserved.")

if __name__ == "__main__":
    main()
