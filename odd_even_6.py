# odd_even_6.py

def isodd(n):
    if n % 2:
        return True
    else:
        return False

# exercise
def isodd2(n):
    return bool(n % 2)

print(f'{isodd2(42) = }')
print(f'{isodd2(-21) = }')
print(f'{isodd2(123) = }')
#print(f'{isodd(42) = }')
#print(f'{isodd(-21) = }')
#print(f'{isodd(123) = }')
