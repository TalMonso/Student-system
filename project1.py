import datetime
now = datetime.datetime.now()


name = str(input("Hello and welcome to my calculator, what is your name? "))
print("Hi " + name + " nice to meet you this is a special calculator, I would need two numbers from you ")


number_1 = int(input("First number: "))
number_2 = int(input("Second number: "))


print("Thank you for putting in your number," + str(number_1) + " and " + str(number_2))

if number_1 % 2 == 0:

    print("I can see that the first number is even")
else:

     print("I can see that the first number is odd")
    

if number_2 % 2 == 0:

    print("I can see that the second number is even")
else:

     print("I can see that the second number is odd")
    

if number_1 % 2 == 0 and number_2 % 2 == 0:

    print("Both of them are even")

elif number_1 % 2 == 0 or number_2 % 2 == 0:

    print("One of the number is even")
else:

    print("Both of them are odd")


operator = str(input("Operator you want (+ , - , * , /) : "))

if operator == "+" :

    result = number_1 + number_2 

elif operator == "-" :

    result = number_1 - number_2

elif operator == "*" :

    result = number_1 * number_2

elif operator == "/" :
    if number_2 == 0 :
        print("Error, you cannot divide a number by zero, please try again")

    else:          
        result = float(number_1 / number_2)
    
else:
    print("Invalid input, you have choose + - * / ")



print('the result is:', result )





print("Thank you " + str(name) + " for using the calculator on " + str(now))



