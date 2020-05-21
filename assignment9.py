a = input("enter a sentence")
b = list(a)
d = {}
for i in set(b):
    c = b.count(i)
    d[i] = c
print(d)