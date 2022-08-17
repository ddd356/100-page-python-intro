# ex_19_2.py

import glob

def f():
    return glob.glob('./*.txt', recursive = True)

if __name__ == '__main__':
    print(f())
