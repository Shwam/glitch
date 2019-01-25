#!/usr/bin/env python3
import sys
import random

out = b""
lines = 0
chunk = 0
glitches = 0
with open(sys.argv[1], 'rb') as f:
    line = True
    while line:
        lines += 1
        line = f.readline()
        # keep the header data intact
        if chunk == 0 and (lines < 10 or random.random() < 0.995 and glitches > 0):
            out += line
        else:
            if chunk == 0:
                glitches += 1
                chunk = random.randint(-5, 5)
            if chunk > 0:
                out += line+line+line
                chunk -= 1
            elif chunk < 0:
                chunk += 1

with open(sys.argv[1], 'wb') as f:
    f.write(out)
