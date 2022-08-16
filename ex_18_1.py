# ex_18_1.py

import copy

def sort_by_value(d):
    d1 = list((copy.deepcopy(d)).items())
    d1.sort(key = lambda a: a[1], reverse = True)
    return dict(d1)

def test():
    assert sort_by_value(dict(Rahul=86, Ravi=92, Rohit=75, Rajan=79, Ram=92)) == {'Rohit': 75, 'Rajan': 79, 'Rahul': 86, 'Ravi': 92, 'Ram': 92}

if __name__ == '__main__':
    test()
    print('All tests done')
