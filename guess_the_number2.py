def user_input():
    """Return proper value provided by user.

    :rtype: str
    :return: value provided by user from ["too small", "too big", "you win"]
    """
    possible_input = ["too small", "too big", "you win"]
    while True:
        user_answer = input().lower()
        if user_answer in possible_input:
            break
        print("Input is not in ['too small', 'too big', 'you win']")
    return user_answer


def guess_the_number():
    """Main function for our program."""
    print("Imagine a number between 0 and 1000!")
    print("Press 'Enter' to continue")
    input()
    min_number = 0
    max_number = 1000
    user_answer = ""
    while user_answer != "you won":
        guess = (max_number - min_number) // 2 + min_number
        print(f"Your number is: {guess}")
        user_answer = user_input()
        if user_answer == "too big":
            max_number = guess
        elif user_answer == "too small":
            min_number = guess

    print("Hooray! I guessed!")


if __name__ == '__main__':
    guess_the_number()
