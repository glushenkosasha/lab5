class Rational:
    def __init__(self, numer, den=1):

        if type(numer) == str:
            self.numer = int(numer.split('/')[0])
            self.den = int(numer.split('/')[1])
        else:
            self.numer = numer
            self.den = den

        assert self.den != 0

        if self._gcd(self.numer, self.den) != 1:
            a = self._gcd(self.numer, self.den)
            self.numer //= a
            self.den //= a

    @staticmethod
    def _gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def __str__(self):
        return f'{self.numer}/{self.den}'

    def __add__(self, other):
        new_numer = self.numer
        new_den = self.den
        if type(other) == Rational:
            new_numer = self.numer * other.den + other.numer * self.den
            new_den = self.den * other.den
        return Rational(new_numer, new_den)

    def __sub__(self, other):
        new_numer = self.numer
        new_den = self.den
        if type(other) == Rational:
            new_numer = self.numer * other.den - other.numer * self.den
            new_den = self.den * other.den
        return Rational(new_numer, new_den)

    def __mul__(self, other):
        new_numer = self.numer
        new_den = self.den
        if type(other) == Rational:
            new_numer = self.numer * other.numer
            new_den = self.den * other.den
        return Rational(new_numer, new_den)

    def __truediv__(self, other):
        new_numer = self.numer
        new_den = self.den
        if type(other) == Rational:
            new_numer = self.numer * other.den
            new_den = self.den * other.numer
        return Rational(new_numer, new_den)

    def __getitem__(self, key):
        if key == 'n':
            return self.numer
        elif key == 'd':
            return self.den

    def __call__(self):
        return self.numer / self.den


if __name__ == '__main__':
    print(Rational(2, 3) / Rational('1/4'))
    print(Rational(2, 3)())