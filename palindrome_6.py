# palindrome_6.py
for x in range(1,1001):
    s = ''
    b = ''
    for y in str(x):
        s = y + s
    for y in f'{x:b}':
        b = y + b

    if str(x) == s and b == f'{x:b}':
        print(x)
        print(f'{x:b}')
