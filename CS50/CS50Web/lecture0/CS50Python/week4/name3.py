# Demonstrates sys.exit

import sys
'''
if len(sys.argv) < 2:
    sys.exit("Too few arguments") # Demonstrates sys.exit
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")# Demonstrates sys.exit

print("hello, my name is", sys.argv[1])
'''
# Demonstrates list slice

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]: # Demonstrates list slice
    # for arg in sys.argv[1:-1]: #To slice from the back use negative number on the end in bracket
    print("hello, my name is", arg)
