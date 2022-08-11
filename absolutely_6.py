# absolutely_6.py
def absolutelu(num):
    if num >= 0:
        return num
    else:
        return -num

def absolutelu2(num):
    return num if num >= 0 else -num

def absolutelu3(num):
    return abs(num)

def absolutelu4(num):
    return (num, -num)[not bool(num >= 0)]

print(f'{absolutelu(-42) = }')
print(f'{absolutelu2(-42) = }')
print(f'{absolutelu3(-42) = }')
print(f'{absolutelu4(-42) = }')
