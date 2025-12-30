#!/usr/bin/python3
import sys
"addition of all arguments"
b = 0
for i in range(1, len(sys.argv), 1):
    b += int(sys.argv[i])
print(f"{b}")

