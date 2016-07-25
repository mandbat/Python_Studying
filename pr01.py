for ((a, b), c) in [((1, 2), 3), ((1, 2), 3), ('ac', 5)]:
    print(a, b, c)

# D = {'a':1,'b':2,'c':3}
# print(list(D.items()))
# for a,b in D.items():
#     print(a,b)

file = open(r'c:\_read\words for problem.txt')
a = file.readlines()
for line in a[0:10]:
    print(line.rstrip())

S = 'spam'

print([c * (i+1) for (i, c) in enumerate(S)])



a = (1,2,3)
b = (4,5,6)

print(dict(zip(a,(c ** 2 for c in a))))
print(dict(zip(a,b)))
print(list(zip(a,(c ** 3 for c in a))))
print(list(zip(a,b)))

