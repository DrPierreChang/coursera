name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
fin = open(name)

counts = dict()

for line in fin:
    if line.startswith('From '):
        email = line.split()[1]
        counts[email] = counts.get(email, 0) + 1
# Variant 1
#m = max(counts, key = counts.get)
#print(m, counts[m])

# Variant 2

bigemail = None
bigcount = None

for k, v in counts.items():
    if bigemail is None or v > bigcount:
        bigemail = k
        bigcount = v

print(bigemail, bigcount)


