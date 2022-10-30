# 1

print('\n#1\n')


class Iterator:

    def __init__(self, num):
        self.num = num
        self.number = 0
        self.a = 0
        self.b = 1
        self.c = self.a + self.b

    def __iter__(self):
        return self

    def __next__(self):
        if self.number >= self.num:
            raise StopIteration
        elif self.number == 0:
            self.number += 1
            return 0
        elif self.number == 1:
            self.number += 1
            return 1
        else:
            self.c = self.a + self.b
            self.a = self.b
            self.b = self.c
            self.number += 1
        return self.b


for i in Iterator(10):
    print(i)

# 2

print('\n#2\n')


def generator(num):
    a = 0
    b = 1
    c = a + b
    for i in range(num):

        if i >= num:
            break
        elif i == 0:
            yield 0
            i += 1
        elif i == 1:
            yield 1
            i += 1
        else:
            c = a + b
            a = b
            b = c
            yield b
            i += 1


for elem in generator(10):
    print(elem)

#3
print('\n#3\n')

g = (number * number for number in range(10))
for elem in g:
    print(elem)
