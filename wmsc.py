import random
x = ['l','c','w']
a = []
b = []
c = []
a.append(x[random.randint(0,2)])
x.remove(a[0])
b.append(x[random.randint(0,1)])
x.remove(b[0])
c.append(x[0])
print("Kids born in east francee")
print(a)
print("kids born in sweden")
print(b)
print("kids born in russia")
print(c)
