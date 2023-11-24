import random

number = random.randint(0, 100)


def get_usr_input():
    guess = input("\nEnter a number: ")
    if guess.isdigit():
        guess = int(guess)
        if guess <= 0:
            print("\nEnter a number bigger than 0 .")
            exit()
    else:
        print("\nEnter a number next time.")

    return guess


def compare():
    usr_input = get_usr_input()
    if usr_input == number:
        print(f"You won !")
        exit()
    elif usr_input > number:
        print("Lower!")
    elif usr_input < number:
        print("Higher!")


try:

    while True:
       compare()

except Exception:
    print()
