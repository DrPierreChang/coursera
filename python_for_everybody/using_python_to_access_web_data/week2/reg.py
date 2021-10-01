import re

fin = open('mbox-short.txt')

for line in fin:
    line = line.rstrip()
    if re.search('From: ', line):
        print(line)