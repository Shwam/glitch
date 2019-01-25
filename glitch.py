#!/usr/bin/env python3
import sys
import random

def metadata(fname):
    md = dict()
    content = None
    with open(fname, 'rb') as f:
        content = f.read()
    for i in range(0, len(content)):
        if content[i] == 0xff:
            if content[i+1] == 0xda:
                # start of scan
                md['start'] = i+2
            elif content[i+1] == 0xd9:
                # end of image
                md['end'] = i
    return md

def glitch(fname):

    md = metadata(fname)

    out = b""
    content = None
    processed = 0
    glitches = 0

    with open(fname, 'rb') as f:
        content = f.read()
        header = content[:md['start']]
        footer = content[md['end']:]
        #content = content[md['start']:md['end']

    for line in content.split(b"\n"):
        processed += len(line) + len(b"\n")
        # keep the header data intact
        if processed < md['start'] or processed >= md['end'] or b"\xff\xda" in line or b"\xff\xd9" in line:
            out += line+b"\n"
            continue
        if glitches < 1:
            glitches += 1
            continue
        if random.random() < 0.995:
            out += line + b"\n"
        else:
            while random.choice((True,False)):
                out += line+b"\n"
        while len(out) < processed:
            out += bytes(chr(random.randint(0,254)), "utf8")

    with open(fname, 'wb') as f:
        f.write(out)

if __name__ == "__main__":
    for i in range(1):
        glitch(sys.argv[1])
