# min_max_ex_12.py
def min_max(i):
    l = len(i)
    max = min = None 
    x = 0
    if l == 0:
        raise ValueError('Argument should be non-empty iterable')
    while x < l:
        if x == 0 or i[x] > max:
            max = i[x]
        if x == 0 or i[x] < min :
            min = i[x]
        x += 1
    return max, min

