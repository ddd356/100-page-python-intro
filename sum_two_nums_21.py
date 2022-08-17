# sum_two_nums.py
import ast
import sys
import functools

try:
    #num1, num2 = sys.argv[1:]
    a = sys.argv[1:]
    #total = ast.literal_eval(num1) + ast.literal_eval(num2)
    s = functools.reduce(lambda x, y: x + ast.literal_eval(y), a, 0)
    p = functools.reduce(lambda x, y: x * ast.literal_eval(y), a, 1)
    avg = s / len(a)
except ValueError:
    sys.exit('Error: Please provide exactly two numbers as arguments')
except TypeError:
    sys.exit('Error: Please provide exactly two numbers as arguments')
else:
    print(f'Sum of {a} = {s}')
    print(f'Product of {a} = {p}')
    print(f'Average of {a} = {avg}')
