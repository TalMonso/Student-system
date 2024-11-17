#DiceRolling
import random


def print_dice(number):
    if number == 1:
        print("-----")
        print("|   |")
        print("| * |")
        print("|   |")
        print("-----")
    elif number == 2:
        print("-----")
        print("|*  |")
        print("|   |")
        print("|  *|")
        print("-----")
    elif number == 3:
        print("-----")
        print("|*  |")
        print("| * |")
        print("|  *|")
        print("-----")
    elif number == 4:
        print("-----")
        print("|* *|")
        print("|   |")
        print("|* *|")
        print("-----")
    elif number == 5:
        print("-----")
        print("|* *|")
        print("| * |")
        print("|* *|")
        print("-----")
    elif number == 6:
        print("-----")
        print("|* *|")
        print("|* *|")
        print("|* *|")
        print("-----")

choice = "y"
print("This is a dice rolling stimlator")
while choice == "y":
    random_number = random.randint(1,6)
    print_dice(random_number)
    choice = input("y - to roll again or any other key to exit: ")

