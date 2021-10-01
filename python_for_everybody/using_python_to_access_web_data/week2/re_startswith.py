import re

fin = open('mbox-short.txt')

for line in fin:
    line = line.rstrip()
    #if re.search('^From: ', line):
    #if re.search('^X.*: ', line):
    #if re.search('^X-\S+:', line):
    if re.search('^From stephen.', line):
        print(line)