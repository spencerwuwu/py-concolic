#!/usr/bin/env python3
import sys
import os

os.chdir(os.path.dirname(__file__))
pyex = sys.argv[1]
dirs = os.listdir("pyex_leetcode/")
for py in dirs:
    if ".py" in py:
        q_dir = "queries/" + py.replace(".py", "")
        os.system("mkdir -p " + q_dir)
        cmd = pyex + " -q " + q_dir + " -m 30 pyex_leetcode/" + py
        os.system(cmd)

