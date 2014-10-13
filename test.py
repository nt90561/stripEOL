# -*- coding: utf-8 -*-

out = open("output.txt", "w")
para = []

with open("test.csv", "r") as f:
    for line in f:
        if len(line) >= 54:
            para.append(line.lstrip().strip("\r\n"))
        else:
            para.append(line.lstrip())
            out.write("".join(para))
            para = []

out.close()
