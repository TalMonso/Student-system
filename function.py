#def silly ():
 #   for i in range(10):
  #      print("this is silly thing to do")


#for i in range(10):
 #   silly()

#def function (x,y):
 #   if x % y == 0:
  #      return x / y
   # elif y % x == 0:
    #    return y / x
    #else:
     #   return 0


#res = function(1000 , 1)
#print(res)


number = int(input("A number to square: "))
def square():
  print(number ** 2)
   
square()

#def stars (x=10):
 #   for i in range(0 , x):
  #      number_of_stars = x - i
   #     print(number_of_stars * "*")


#stars()

def profit(small_cups, large_cups, price_small=3, price_large=5):
  money = (small_cups * price_small)+(large_cups * price_large)
  print("we earned", money, "shekels")

profit(large_cups = 10, small_cups = 10)
