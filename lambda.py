from functools import reduce
def myfunc(x, y): return x + y


print(myfunc(1, 2))

l = range(1, 10)
print(list(l))
print(reduce(myfunc, l))
