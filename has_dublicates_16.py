# has_dublicates_16.py

def has_dublicates(i):
    return len(i) != len(set(i))

def test():
    assert has_dublicates('pip') == True
    assert has_dublicates((3,2)) == False

if __name__ == '__main__':
    test()
    print('Tests done')
