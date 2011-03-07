#!/usr/bin/python
"""
Recursively copies files from location with bad blocks into safe one.
Internally calls ddrescue.

By Denis Malinovsky <dmalinovsky@gmail.com>
"""
import os
import subprocess
import sys

if len(sys.argv) < 3:
    sys.exit("Usage: %s [options] infolder outfolder" % sys.argv[0])

infolder = sys.argv[-2]
outfolder = sys.argv[-1]

for root, dirs, files in os.walk(infolder):
    if not files:
        continue
    root = os.path.relpath(root, infolder)
    outpath = os.path.join(outfolder, root)
    if not os.path.exists(outpath):
        os.makedirs(outpath)
    for file_ in files:
        subprocess.call(['dd_rescue'] + sys.argv[1:-2] +
                [os.path.join(infolder, root, file_), os.path.join(outpath,
                    file_)])
