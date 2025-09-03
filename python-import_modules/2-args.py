#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    arg_num = len(sys.argv)
    if arg_num == 1:
        print("0 arguments.")
    elif arg_num == 2:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(arg_num))
        for i in range(1, arg_num):
            print("{}: {}".format(i, sys.argv[i]))
