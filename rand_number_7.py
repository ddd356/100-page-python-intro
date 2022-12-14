# rand_number_7.py
import random

# gives back an integer between 0 and 10 (inclusive)
rand_int = random.randrange(11)

print('I have thought of a number between 0 and 10.')
print('Can you guess it within four attempts?\n')
for _ in range(4):
    guess = int(input('Enter your guess: '))
    if guess == rand_int:
        print('Wow, you guessed it right!')
        break
    elif guess > rand_int:
        print('Oops! Your guess is too high')
    else:
        print('Oops! Your guess is too low')
else:
    print('\nOh no! You are out of chances. Better luck next time.')
