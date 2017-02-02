#! /usr/bin/env python3

import subprocess
import sys

def determine_runner(script_path):
    dot_split = script_path.split(".")
    return ["ruby", script_path] if dot_split[-1] == "rb" else ["python3", "-m", script_path]

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 %s <script.path> <iters>" % __file__)
        exit(1)
    else:
        running_sum = 0
        limit = int(sys.argv[2])

        for _ in range(limit):
            out = subprocess.run(determine_runner(sys.argv[1]), stdout=subprocess.PIPE)
            running_sum += float(out.stdout)

        print("Mean: %s" % (running_sum / limit))
