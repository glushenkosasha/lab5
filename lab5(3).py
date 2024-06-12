from lab5 import Rational


def string(s):
    new = s.split('/')
    obj = Rational(int(new[0]), int(new[1]))
    return obj


result = open('result.txt', 'w')
with open('input01.txt') as f:
    for line in f:
        if line.split() != []:
            data = [el for el in line.split()]
            try:
                res = Rational(int(data[0]))
            except ValueError:
                res = string(data[0])

            for num in range(len(data) - 1):
                if data[num] in '+-*':
                    try:
                        obj = Rational(int(data[num + 1]))
                    except ValueError:
                        obj = string(data[num + 1])

                    if data[num] == '+':
                        res += obj
                    elif data[num] == '-':
                        res -= obj
                    elif data[num] == '*':
                        res *= obj
            result.write(f'{res}, \n')