from functools import reduce

colors = [
    'red',
    'green',
    'blue',
    'yellow',
    'pink'
]

a = ["ABC", 10]

print(colors)
print(a)

for c in colors:
    print(c.upper())

for i in a:
    print(i)

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(l[2:8:2])
m = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(l + m)

t = (1, 2, 3)
print(t)
print(t[1])

# t[1] = 4
ll = list(t)
print(ll)


d = {'a': 100, 'b': 200, 'c': 300}

print(d)

for k, v in d.items():
    print(f'{k}: {v}')

for k in d.keys():
    print(k)
for v in d.values():
    print(v)


a = range(1, 11)


def double(n: int) -> int:
    """Returns a doubled argument."""
    return n * 2


# map
print(list(map(double, a)))
print(list(map(lambda n: n * 3, a)))
print(list([n * 5 for n in a]))


def is_odd(n: int) -> bool:
    """"Returns whether it is odd."""
    return n % 2


# filter
print(list(filter(is_odd, a)))
print(list(filter(lambda n: n % 2, a)))
print([n for n in a if n % 2])


def sum(x: int, y: int) -> int:
    """Returns the sum of two arguments"""
    return x + y


# reduce
print(reduce(sum, a))
print(reduce(lambda x, y: x + y, a))


c = [1, 2, 3]
d = [4, 5, 6]
print([x * y for x in c for y in d])


s = set(['red', 'blue', 'yellow'])
t = set(['red', 'green', 'blue'])

print(s)
print(t)
print(s - t)
print(s | t)
print(s & t)
print(s ^ t)
print('red' in s)
s.add('black')
print(s)
