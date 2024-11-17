#letters = "abcdefghijklmnopqrstuvwxyz"
#gimatria_dictionary = dict()
#index = 1
#for let in letters:
 #   gimatria_dictionary[let] = index 
  #  index += 1

#result = 0
#word = input('please enter a word')
#for letter in word:
 #   result += gimatria_dictionary[letter]
#print(result)

        
#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#new_numbers = list()
#for item in numbers :
    #new_numbers.append(item*10)

#print(numbers)
#print(new_numbers)


numbers = list()
for i in range(10):
    x = int(input('please enter number: '))
    if x < 0:
        break
    numbers.append(x)

average = sum(numbers) / len(numbers)
print("The average is: ",average)



