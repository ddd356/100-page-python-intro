# fizzbuzz_6.py
for x in range(1, 101):
    if (not x % 3) and (not x % 5):
        print('FizzBuzz')
        continue
    if not x % 5:
        print('Buzz')
        continue
    if not x % 3:
        print('Fizz')
        continue
    print(x)
