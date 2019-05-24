#!/usr/bin/env python
import sys
import os
def main():
    benchmark_files = sorted([os.path.join(root, file)
                              for root, dirs, files in os.walk("./queries") for file in files])

    for ben in benchmark_files:
        if ".py" in ben:
            continue
        
        with open(ben, "r") as source:
            code = source.read() + "\n"
            lines = code.split("\n")
        with open(ben, "w") as dest:
            for line in lines:
                if "set-logic" not in line and "set-option" not in line:
                    dest.write(line + "\n")

        print(ben)

if __name__ == '__main__':
    main()
