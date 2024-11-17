#def combine_coins(coin , numbers): return ',' .join([coin + str(i) for i in numbers])
#print(combine_coins('$',range(5)))

class Animal:


    def __init__(self):
        self.age = 0
        


    def birthday(self, age, birthday):
        self.age += birthday

    


def main():
    animal_1 = Animal()
    animal_1.birthday(10)
   


    animal2 = Animal()
    animal2.birthday(9)

    animal2.birthday()
    animal_1.birthday()
    print(animal_1.birthday)
main()


    


    
        
