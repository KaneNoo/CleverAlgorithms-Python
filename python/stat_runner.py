#! /usr/bin/env python3

"""
This script assumes that all the demo scripts can be ran with a csv flag which
will output the log trace as CSV (to stdout).

It further assumes that the last line of the CSV output is some kind of
description about the best solution arrived at.
"""

import os
import subprocess
import sys

def determine_runner(script_path):
    dot_split = script_path.split(os.extsep)
    if dot_split[-1] == "rb":
        return ["ruby", script_path, "csv"]
    else:
        return ["python3", "-m", script_path, "csv"]

def write_stat_doc(doc_fname, doc):
    with open(doc_fname, "w") as stat_doc:
        stat_doc.write(doc)

def __make_data_dir_name(runner, script_path):
    parsed_path = []
    if runner == "python3":
        parsed_path = script_path.split(".")
    else:
        parsed_path = script_path.split(os.path.sep)

    return "-".join(parsed_path)

def make_data_dir_path(runner, script_path):
    return os.path.join(os.curdir, "stats", __make_data_dir_name(runner, script_path))

def ensure_data_dir_exists(runner, script_path):
    data_dir_path = make_data_dir_path(runner, script_path)
    if not os.path.isdir(data_dir_path) and not os.path.isfile(data_dir_path):
        print("data dir for %s does not exist, creating..." % script_path)
        os.mkdir(data_dir_path)

def write_data_dump(runner, script_path, fname, dump):
    data_fname = os.path.join(make_data_dir_path(runner, script_path), fname)
    with open(data_fname, "w+") as data:
        data.write(dump)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 %s <script.path> <iters>" % __file__)
        exit(1)

    stats_dir = os.path.join(os.curdir, "stats")
    if not os.path.isdir(stats_dir) and not os.path.isfile(stats_dir):
        print("stats directory does not exist, creating...")
        os.mkdir(stats_dir)

    running_sum = 0
    limit = int(sys.argv[2])
    runstring = determine_runner(sys.argv[1])
    ensure_data_dir_exists(runstring[0], sys.argv[1])

    for runcount in range(limit):
        out = subprocess.run(runstring, stdout=subprocess.PIPE)
        write_data_dump(runstring[0], sys.argv[1], "%s.csv" % (runcount + 1), out.stdout.decode("utf-8"))
