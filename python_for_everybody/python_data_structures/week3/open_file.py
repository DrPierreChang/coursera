fname = input("Enter file name: ")

try:
    fin = open(fname, 'r')
except:
    print('There is no such file')
    quit()

for line in fin:
    line = line.strip()
    if line.startswith('C'):
        print(line)