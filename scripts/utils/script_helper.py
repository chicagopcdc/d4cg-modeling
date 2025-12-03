# scripts/utils/repo_helper.py

import os, sys, subprocess, time

def enforce_repo_root():
    try:
        # Get the top-level directory of the current Git repo
        repo_root = subprocess.check_output(
            ["git", "rev-parse", "--show-toplevel"],
            stderr=subprocess.DEVNULL
        ).decode().strip()
    except subprocess.CalledProcessError:
        print("Error: Not inside a Git repository.")
        sys.exit(1)

    # Compare to current working directory
    cwd = os.getcwd()
    if os.path.abspath(cwd) != os.path.abspath(repo_root):
        print(f"\nPlease run this script from the repository root:\n   {repo_root}\n")
        print(f"   You are currently in:\n   {cwd}\n")
        sys.exit(1)


def elapsed_time(start):
    seconds = time.time() - start
    m, s = divmod(seconds, 60)
    return f"{int(m)}m {s:.2f}s"