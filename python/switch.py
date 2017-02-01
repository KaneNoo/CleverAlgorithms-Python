import sys

def decide():
    if len(sys.argv) == 2:
        flag = sys.argv[1].lower()

        if flag == "true":
            return True
        elif flag != "false":
            print("Usage: python3 %s <true|false>" % sys.argv[0])
            exit(1)
    return False
