from random import randint
number = randint(1, 101)
guessed = 0
while guessed != number:
    try:
        guessed = int(input('Guess the number '))
        if guessed > number:
            print('Too big!')
        elif guessed < number:
            print('Too small!')
    except ValueError:
        print('To nie jest liczba')

print('You win!')
