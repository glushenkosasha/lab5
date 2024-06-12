from lab5 import Rational


class RationalList:
    def __init__(self, array):
        self.array = list(array)

    def sum(self):
        return sum(self.array)

    def __str__(self):
        return str(self.array)

    def __getitem__(self, item):
        return self.array[item]

    def __setitem__(self, key, value):
        if type(value) == Rational:
            self.array[key] = value()
        else:
            self.array[key] = value

        return self.array

    def __len__(self):
        return len(self.array)

    def __add__(self, other):
        if type(other) == RationalList:
            for x in list(other):
                self.array.append(x)
        elif type(other) == Rational:
            self.array.append(other())

        return self.array

    def __iadd__(self, other):
        if type(other) == RationalList:
            for x in other:
                if x not in self.array:
                    self.array.append(x)

        elif type(other) == Rational:
            if other() not in self.array:
                self.array.append(other())

        return self.array


if __name__ == '__main__':
    a = RationalList([])
    b = RationalList([2, 4])
    b[0] = Rational(4, 5)
    print(b + 4)
    print(a + Rational(5))
    a += RationalList([1, 3, 4])
    print(a)