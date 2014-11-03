# -*- coding: utf-8 -*-
import os

def stripEOL(in_file, out_file):
    out = open(out_file, "w")
    para = []
    switch = 0
    with open(in_file, "r") as f:
        for line in f:
            line = line.decode('utf-8')

            char = 0
            for word in line:
                if word.isspace() or word.isdigit():
                    char -= 1
            char = len(line) + char/2

            if line[0:4] == u"上列被告":
                switch = 1

            if not len(line):
                switch = 0
            elif char >= 28 and switch == 1:
                para.append(line.lstrip().strip("\r\n"))
            else:
                para.append(line.lstrip())
                out.write("".join(para).encode('utf-8'))
                para = []
    out.close()

def files_pipe(input_path, output_path, func=0):

    file_list = []
    for (a, b, c) in os.walk(input_path):
        file_list.extend(c)
    file_list = tuple(file_list)

    for filename in file_list:
        textfile = os.path.join(input_path, filename)
        newfile = os.path.join(output_path, filename)
        file = open(newfile, 'w+')
        file.close()
        if func == 1:
            stripEOL(textfile, newfile)

files_pipe('input/', 'output', 1)

