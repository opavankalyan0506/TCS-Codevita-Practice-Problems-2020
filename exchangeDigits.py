from itertools import permutations

a, b = input().split()
l = permutations(a)
res = []
for i in l:
  res.append(int(''.join(i)))
res.sort()
flag = True

for i in res:
  if i > int(b):
    flag = False
    print(i)
    break
if flag:
  print(-1)
