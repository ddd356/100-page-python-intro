# ex_13_1.py

import functools
import pytest


def test():
    assert product([-4, 2.3e12, 77.23, 982, 0b101])
    assert product([-4, 2.3e12, 77.23, 982, 0b101])
    assert product(range(2, 6))

def test_exception():
    with pytest.raises(TypeError) as e:
        assert 'reduce() of empty iterable with no initial value' in product(())
    
        assert 'can\'t multiply sequence by non-int of type \'str\'' in product(['a', 'b'])

def product(iterable):
    return functools.reduce(lambda x,y: x * y, iterable)

if __name__ == '__main__':
    test()
    test_exception()
    print('All tests done')


