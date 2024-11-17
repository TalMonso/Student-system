number_1 = int(input("enter number 1: "))
number_2 = int(input("enter number 2: "))

print("options: ")
print("1. number_1 / number_2")
print("2. is number 1 even? ")
print("3. hot or cold")
selection = int(input("enter your selection: "))

if selection == 1:
    # number_1 / number_2 
    if number_2 != 0:
        result = number_1 / number_2
    else:
        # number_2 == 0
        print("number_2 equal to zero")
        result = 0
elif selection == 2:
    # Is number_1 even
    if number_1 % 2 == 0:
        print("number_1 is even")
    else:
        print("number_1 is odd")
elif selection == 3: 
    # Hot cold
    temp = number_1
    if temp > 20:
        print("Hot")
    else:
        print("Cold")
else:
    print("invalid input. option" + str(slection) + "not supported")



