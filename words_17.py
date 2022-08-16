# words_17.py

import string

def words(s):
    s1 = s.translate(s.maketrans(string.punctuation, ' ' * len(string.punctuation)))
    return s1.split()

def test():
    assert words('"Hi", there! How *are* you? All fine here.') == ['Hi', 'there', 'How', 'are', 'you', 'All', 'fine', 'here']
    assert words('This-Is-A:Colon:Separated,Phrase') == ['This', 'Is', 'A', 'Colon', 'Separated', 'Phrase']

if __name__ == '__main__':
    test()
    print("All tests done")
