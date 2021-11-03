a = [1,2,3,4,5]
a[0] = 5
a[1] = len(a)
print(a)
b = a[0:2]
c = []
for x in b:
    c.append(x*5)
print(c)
d = [x+10 for x in b]
for x in d:
    if (x>20):
        print(x)
sumA = sum(a)
print(sumA)


