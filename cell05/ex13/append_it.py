import sys

args = sys.argv[1:]

if len(args) == 0:
    print("none")
else:
    for arg in args:
        if arg.endswith("ism"):
            continue
        print(arg + "ism")