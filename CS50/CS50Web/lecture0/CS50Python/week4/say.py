# Demonstrates pip-installed package

import cowsay
import sys
from saings import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])
