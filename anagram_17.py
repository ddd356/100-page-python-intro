# anagram_17.py

def anagram(s1, s2):
    l1 = sorted(s1.lower())
    l2 = sorted(s2.lower())
    return l1 == l2

def test():
    assert anagram('god', 'Dog') == True
    assert anagram('beat', 'table') == False
    assert anagram('Beat', 'abet') == True

if __name__ == '__main__':
    test()
    print('Tests done')
