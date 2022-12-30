#!/usr/bin/env python3
import re

for i in range(int(input())):
    print(bool(re.match("^[\+-]?\d*\.\d+$", input())))