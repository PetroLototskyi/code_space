# Uses command-line argument

import sys
'''
if len(sys.argv) == 1:
    print("meow")
elif len(sys.argv) == 3 and sys.argv[1] == "-n":
    n = int(sys.argv[2])
    for _ in range(n):
        print("meow")
else:
    print("usage: meows11.py [-n NUMBER]")
'''
# Uses command-line argument

import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", default=1, help="number of times to meow", type=int) # this is method in parcer object
args = parser.parse_args() #look into all command line arguments

for _ in range(args.n): 
    print("meow")
