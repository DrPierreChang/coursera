astr = input()
try:
    istr = int(astr)
except:
    print("Error!!!")
    quit()


print('First', istr)

astr = input()
try:
    istr = int(astr)
except:
    istr = -1
print('Second', istr)
