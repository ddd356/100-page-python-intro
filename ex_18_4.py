# ex_18_4.py

import functools

def f(l):
    return functools.reduce(lambda x,y: x + pow(y, 2) if pow(y, 2) < 50 else x, l, 0)

def test():
    assert f((7.1, 1, -4, 8, 5.1, 12)) == 43.01

if __name__ == '__main__':
    test()
    print('Tests done')
