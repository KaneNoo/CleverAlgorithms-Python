#! /usr/bin/env python3

import subprocess
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 %s <script.package.path> <iters>" % __file__)
        exit(1)
    else:
        running_sum = 0
        limit = int(sys.argv[2])

        for _ in range(limit):
            out = subprocess.run(["python3", "-m", sys.argv[1]], stdout=subprocess.PIPE)
            running_sum += float(out.stdout)

        print("Mean: %s" % (running_sum / limit))
