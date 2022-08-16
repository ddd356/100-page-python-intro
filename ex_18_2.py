# ex_18_2.py

def word_slices(w):
    if len(w) < 2:
        return [w]
    return list(helper(w))

def helper(w):
    for i in range(0, len(w)-1):
        for j in range(i+2, len(w)+1):
            yield w[i:j]

def test():
    assert word_slices('table') == ['ta', 'tab', 'tabl', 'table', 'ab', 'abl', 'able', 'bl', 'ble', 'le']

if __name__ == '__main__':
    test()
    print('Tests done')
