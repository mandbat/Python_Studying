# списки
title = ' списки '
print('\n' + '*' * 7 + title + '*' * 7)
a = [1,2,3]
a[0] = 0
a.append(4)
del a[2]
print(a)

# кортеж - нельзя изменять
title = ' кортежи '
print('\n' + '*' * 7 + title + '*' * 7)
b = (1,2,3)
print(b)

# словари
title = ' словари '
print('\n' + '*' * 7 + title + '*' * 7)
b = {1:1,2:2,3:3}
b["key_str"] = 4
b[1] = "str value"
print(b)

fields = ('name','age')
record = dict.fromkeys(fields,'?')
print(record)

# множества
title = ' множества '
print('\n' + '*' * 7 + title + '*' * 7)
c = {1,2,3}
d = {2,3,4}
print(c.union(d))

# map, lambda
title = ' map, lambda '
print('\n' + '*' * 7 + title + '*' * 7)
a = (1,2,4)
x = list(map(lambda x: x**2, a))
print(x)

m = [{'name': 'name01', 'age': 34}, {'name': 'name02', 'age': 35}]
print(list(map((lambda x: x['name']),m)))
print(list(map((lambda x: x['age']),m)))


# dict + list + zip - генераторы
title = ' dict + list + zip - генераторы '
print('\n' + '*' * 7 + title + '*' * 7)
print(dict(zip(a,(c ** 2 for c in a))))
print(dict(zip(a,b)))
print(list(zip(a,(c ** 3 for c in a))))
print(list(zip(a,b)))
