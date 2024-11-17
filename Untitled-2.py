#get_size = lambda i : len(i)
#i1 = []
#i2 = [1,2,3]
#i3 = ['tal', 50, {},'']
#print(get_size(i1), get_size(i2), get_size(i3)) 

#person1 = {'name' : 'tal', 'age' : 25, 'address' : 'Beer sheva'}
#person2 = {'name' : 'amit', 'age' : 35, 'address' : 'Eilat'}
#person3 = {'name' : 'asaf', 'age' : 22, 'address' : 'Netivot'}
#person4 = {'name' : 'niv', 'age' : 28, 'address' : 'Tel aviv'}
#persons = [person1, person2, person3, person4]
#get_age = lambda person : person['age']
#sorted_persons =  sorted(persons , key =get_age)
#print(persons[0])
#print(sorted_persons[0])

#my_list = [10 ,2 ,-4 ,12 ,52]
#print(sorted(my_list))
#print(sorted(my_list, reverse=True))

#my_tuple = (1 ,7, -12 ,25 ,-4 ,40)
#print(sorted(my_tuple ,reverse=True))
#x = (100, )
#print(x ,type(x))

def delete_from_set(x : set):
    to_delete = input("please enter a number: ")
    to_delete = int(to_delete)
    x.discard(to_delete)
    return(x)
my_set = {1,2,4,2,5,7}
print(delete_from_set(my_set))

