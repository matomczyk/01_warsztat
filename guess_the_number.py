import random


def get_number():
    """Get number from user.

    Try until user give proper number.

    :rtype: int
    :return: given number as int
    """
    while True:
        try:
            result = int(input("Guess the number: "))
            break
        except ValueError:
            print("It's not a number")

    return result


def guess_the_number():
    """Main function with our game."""
    secret_number = random.randint(1, 100)
    given_number = get_number()
    while given_number != secret_number:
        if given_number < secret_number:
            print("Too small!")
        else:
            print("Too big!")
        given_number = get_number()
    print("You Win!")


if __name__ == '__main__':
    guess_the_number()
