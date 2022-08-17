# ex_18_3.py

def f(l):
    return list(map(lambda a: pow(a, 2) if a % 2 == 0 else pow(a, 3), l))

def test():
    assert f([321, 1, -4, 0, 5, 2]) == [33076161, 1, 16, 0, 125, 4]

if __name__ == '__main__':
    test()
    print('All tests done')
