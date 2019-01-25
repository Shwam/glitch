#!/usr/bin/env python3
import sys
import random

out = b""
lines = 0
with open(sys.argv[1], 'rb') as f:
    lines = []
    line = True
    while line:
        line = f.readline()
        if line:
            lines.append(line)
    
    glitched = lines[10:-10]
    for i in range(len(glitched)):
        if random.random() < 0.001:
            j = random.choice(range(len(glitched)))
            glitched[i], glitched[j] = glitched[j], glitched[i]
    lines = lines[:10] + glitched + lines[-10:]


with open(sys.argv[1], 'wb') as f:
    for line in lines:
        f.write(line)
