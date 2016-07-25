def func1():
    return 1

def func2():
    return 2

a = [func1,func2]
print(a[0]())
print(a[1]())