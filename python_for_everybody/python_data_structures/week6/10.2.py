fname = input('Enter the file name: ')

if len(fname) < 1:
    fname = 'mbox-short.txt'

fin = open(fname)
counts = dict()

for line in fin:
    if line.startswith('From '):
        line = line.rstrip().split()[-2][:2]
        counts[line] = counts.get(line, 0) + 1

counts = sorted([(k, v) for k, v in counts.items()])

for k, v in counts:
    print(k, v)