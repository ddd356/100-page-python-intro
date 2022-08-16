# ex_13_2.py

def remove_dunder(x):
    return [n for n in dir(x) if '__' not in n]

def remove_dunder2(x):
    return list(filter(lambda a: '__' not in a,dir(x)))

def remove_dunder1(x):
    return list(filter(lambda a: a[0:2] != '__' and a[-2:] != '__' ,dir(x)))

def test():
    assert remove_dunder(list) == ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
    assert remove_dunder(tuple) == ['count', 'index']

if __name__ == '__main__':
    test()
    print('Tests passed')
