#! /usr/bin/env python3

"""
This script assumes that all the demo scripts can be ran with a csv flag which
will output the log trace as CSV (to stdout).

It further assumes that the last line of the CSV output is some kind of
description about the best solution arrived at.
"""

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
