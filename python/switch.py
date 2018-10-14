import sys

def decide():
    if len(sys.argv) == 2:
        return sys.argv[1]
    return "human"
