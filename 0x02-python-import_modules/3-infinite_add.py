#!/usr/bin/python3
import sys
if __name__ == "__main__":
    var = 0
    for i in range(1, len(sys.argv)):
        var = var + int(sys.argv[i])
    print(var)
