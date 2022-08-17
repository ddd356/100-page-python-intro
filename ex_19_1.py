# ex_19_1.py

def f():
    s = 0
    with open('test_19_1.txt', mode = 'r', encoding = 'ascii') as f:
        for op_line in f:
            a = float(op_line)
            s = s + a
    print(s)

if __name__ == '__main__':
    f()
