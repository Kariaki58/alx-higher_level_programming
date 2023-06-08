#!/usr/bin/python3
import sys


args = sys.argv
convertToInt = 0
for i in range(1, len(args)):
	convertToInt += int(args[i])
print("{}".format(converToInt))
