import sys
if __name__ == "__main__":
    """print arguments"""
    import sys
    num_arg = len(sys.argv) - 1

    if num_arg == 0:
        print("0 arguments.")
    elif num_arg == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))
