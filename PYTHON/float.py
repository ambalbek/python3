#!/usr/bin/env python3
import re

lis1 = []
for i in range(int(input())):
    b = (input())
    lis1.append(b)


for i in lis1:

	print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', i)))