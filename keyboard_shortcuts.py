#keyboard_shortcuts = {"copy": "ctrl + c", "paste": "ctrl + v", "cut": "ctrl + x", "undo": "ctrl + z"}

#print(keyboard_shortcuts["paste"])


def square(num):   #דוגמה לפונקציה map
    return num ** 2

list_of_numbers = [2, 4, 6, 8,10]
result = map(square,list_of_numbers)
print(list(result))






