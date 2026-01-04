"""
Benchmarks uv vs poetry installation speed WITHOUT lock files.

This tests the full process: figuring out which package versions work together
(dependency resolution) + downloading and installing them.

This is what happens when you first set up a project or update dependencies.
"""

import subprocess
import time
import shutil
import json
from pathlib import Path
from datetime import datetime


def run_benchmark(tool, project_dir):
    venv_path = project_dir / ".venv"

    # Clean up existing venv and lock file
    if venv_path.exists():
        shutil.rmtree(venv_path)

    if tool == "uv":
        lock_file = project_dir / "uv.lock"
        if lock_file.exists():
            lock_file.unlink()
    elif tool == "poetry":
        lock_file = project_dir / "poetry.lock"
        if lock_file.exists():
            lock_file.unlink()

    # Time the installation
    start = time.time()

    if tool == "uv":
        subprocess.run(
            ["uv", "sync", "--no-install-project"], cwd=project_dir, check=True
        )
    elif tool == "poetry":
        subprocess.run(["poetry", "install", "--no-root"], cwd=project_dir, check=True)

    end = time.time()

    return end - start


# Run benchmarks
poetry_dir = Path("poetry")
uv_dir = Path("uv")

print("Running poetry benchmark...")
poetry_time = run_benchmark("poetry", poetry_dir)
print(f"Poetry: {poetry_time:.2f}s")

print("\nRunning uv benchmark...")
uv_time = run_benchmark("uv", uv_dir)
print(f"UV: {uv_time:.2f}s")

if uv_time < poetry_time:
    winner = "uv"
    speedup = poetry_time / uv_time
else:
    winner = "poetry"
    speedup = uv_time / poetry_time

print(f"\nWinner: {winner} ({speedup:.1f}x faster)")

# Export results
results = {
    "poetry_time": poetry_time,
    "uv_time": uv_time,
    "winner": winner,
    "speedup": speedup,
    "summary": f"Winner: {winner} ({speedup:.1f}x faster)",
}
timestamp = datetime.now().strftime("%Y_%m_%d_%H%M%S")
filename = f"benchmark_no_lock_results_{timestamp}.json"

with open(filename, "w") as f:
    json.dump(results, f, indent=2)

print("\nResults saved to benchmark_with_lock_results.json")
