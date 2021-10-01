di = {'a':10, 'b':1, 'c':22}
# tmp = list()
# for k,v in di.items():
#     tmp.append((v,k))
#
# #print(tmp)
#
# tmp = sorted(tmp, reverse=True)
# #print(tmp)
#
# for v, k in tmp:
#     print(v, k)


print(sorted([(v, k) for k, v in di.items()]))
