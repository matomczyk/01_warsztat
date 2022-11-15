import random


def get_number():
    """Get number from user.

    Try until user give proper number.

    :rtype: int
    :return: given number as int
    """
    while True:
        try:
            result = int(input("Choose a number: "))
            break
        except ValueError:
            print("It's not a number")

    return result


def get_numbers():
    """Get 6 different numbers between 1 and 49.

    :rtype: set
    :return: set with 6 numbers provided by user
    """
    result = set()
    while len(result) < 6:
        number = get_number()
        if 0 < number <= 49:
            result.add(number)

    return result


def print_numbers(numbers):
    """Print given numbers in ascending order.

    :param set numbers: list of numbers
    """
    print(", ".join(str(number) for number in sorted(numbers)))


def drawing_numbers():
    """Choose 6 random numbers.

    :rtype: set
    :return: list with 6 random numbers
    """
    numbers = list(range(1, 50))
    random.shuffle(numbers)
    return set(numbers[:6])


def lotto():
    """Main function with our program."""
    user_numbers = get_numbers()
    print("Your numbers:")
    print_numbers(user_numbers)

    random_numbers = drawing_numbers()
    print("Lotto numbers:")
    print_numbers(random_numbers)

    hits = 6 - len(random_numbers - user_numbers)

    print(f"You hit {hits} {'number' if hits == 1 else 'numbers'}!")


if __name__ == '__main__':
    lotto()
