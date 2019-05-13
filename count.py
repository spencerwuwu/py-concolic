#!/usr/bin/env python3

import sys
import os

if __name__ == "__main__":
    dirs = os.listdir("queries-2/")
    pys = os.listdir("pyex_leetcode/")

    count = 0
    total = 0
    for qdir in dirs:
        total += 1
        if len(os.listdir("queries-2/" + qdir)) != 0:
            count += 1
            print("mv pyex_leetcode/" + qdir + ".py done/")
            os.system("mv pyex_leetcode/" + qdir + ".py done-2/")
        #else:
            #print(qdir)
    print(count)
    print(total)

