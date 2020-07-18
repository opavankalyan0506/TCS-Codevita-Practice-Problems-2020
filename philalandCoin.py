n = input().split()
res = []
for i in n:
  if i.isdigit():
    b = max(list(map(int, list(i)))) + 1
    s = 0
    for j in range(len(i)):
      s = s + (int(i[j])*(b**(len(i)-j-1)))
    res.append(s)
  else:
    p = []
    for j in i:
      if j.isalpha():
        p.append(j)
    b = ord(max(p))-54
    s = 0
    for j in range(len(i)):
      if i[j].isalpha():
        s = s + ((ord(i[j])-55)*(b**(len(i)-j-1)))
      else:
        s = s + (int(i[j])*(b**(len(i)-j-1)))
    res.append(s)
print(min(res))
