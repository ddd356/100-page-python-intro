# num_funcs_module.py

def sqr(n):
    """
    Returns square of the argument
    """
    return n * n

def fact(n):
    """
    Returns factorial of the argument
    """

    try:
        if n < 0:
            raise ValueError
        if not isinstance(n, int):
            raise ValueError

    except ValueError:
        print('Not a positive integer, run the program again')
    else:
        total = 1
        for i in range(2, n+1):
            total *= i
        return total

if __name__ == '__main__':
    num = 5
    print(f'square of {num} is {sqr(num)}')
    print(f'factorial of {num} is {fact(num)}')
