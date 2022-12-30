#!/usr/bin/env python3
import os
if os.path.exists("*ter.tr.txt"):
    os.remove("ter.tr.txt")
else:
    print("The file does not exist")