#!/usr/bin/env python3
"""Prints a grid of random box characters"""

import random

out = ""
for i in range(0, 100):
    for j in range(0, 220):
        out += " " if random.random() > 0.6 else chr(random.randint(9600,9631))
    out += "\n"
print(out)
