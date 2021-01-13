class MyClass:
    def __init__(self):
        self.data = (1, 2, 3, 4, 5)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            self.index += 1
            return self.data[self.index - 1]
        else:
            raise StopIteration


def double(it: iter) -> iter:
    """yieldを利用したイテレータによる数値の2倍処理"""
    for n in it:
        yield n * 2


for n in MyClass():
    print(n)

it = MyClass().__iter__()
while True:
    try:
        n = it.__next__()
        print(n)
    except StopIteration as ex:
        break

for n in double(MyClass()):
    print(n)
