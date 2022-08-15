# ex_13_2.py

def remove_dunder(x):
    return list(filter(lambda a: a[0:2] != '__' and a[-2:] != '__' ,dir(x)))

def test():
    assert remove_dunder(list) == ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
    assert remove_dunder(tuple) == ['count', 'index']

if __name__ == '__main__':
    test()
    print('Tests passed')
