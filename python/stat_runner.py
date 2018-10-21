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

class StatRunner(object):
    
    def __init__(self, script_path, output_encoding="utf-8"):
        self.script_path = script_path
        self.runstring = self.__determine_runner()
        self.runner = self.runstring[0]
        self.output_encoding = output_encoding

        self.__setup()

    def __setup(self):
        stats_dir = os.path.join(os.curdir, "stats")
        if not os.path.isdir(stats_dir) and not os.path.isfile(stats_dir):
            print("stats directory does not exist, creating...")
            os.mkdir(stats_dir)
        self.__ensure_data_dir_exists()

    def __determine_runner(self):
        dot_split = self.script_path.split(os.extsep)
        if dot_split[-1] == "rb":
            return ["ruby", script_path, "csv"]
        else:
            return ["python3", "-m", script_path, "csv"]
    
    def __write_stat_doc(self, doc_fname, doc):
        with open(doc_fname, "w") as stat_doc:
            stat_doc.write(doc)
    
    def __make_data_dir_name(self):
        parsed_path = []
        if self.runner == "python3":
            parsed_path = self.script_path.split(".")
        else:
            parsed_path = self.script_path.split(os.path.sep)
    
        return "-".join(parsed_path)
    
    def __make_data_dir_path(self):
        return os.path.join(os.curdir, "stats", self.__make_data_dir_name())
    
    def __ensure_data_dir_exists(self):
        data_dir_path = self.__make_data_dir_path()
        if not os.path.isdir(data_dir_path) and not os.path.isfile(data_dir_path):
            print("data dir for %s does not exist, creating..." % self.script_path)
            os.mkdir(data_dir_path)
    
    def __write_data_dump(self, runner, script_path, fname, dump):
        data_fname = os.path.join(self.__make_data_dir_path(), fname)
        with open(data_fname, "w+") as data:
            data.write(dump)

    def gather_stats(self, iters):
        for runcount in range(iters):
            print("Run #%s for %s" % (runcount + 1, self.script_path))
            out = subprocess.run(self.runstring, stdout=subprocess.PIPE)
            self.__write_data_dump(
                self.runner,
                self.script_path,
                "%s.csv" % (runcount + 1),
                out.stdout.decode(self.output_encoding)
            )

        print("Done. Find stats in %s" % self.__make_data_dir_path())

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 %s <script.path> <iters>" % __file__)
        exit(1)

    limit = int(sys.argv[2])
    script_path = sys.argv[1]

    runner = StatRunner(script_path)
    runner.gather_stats(limit)
