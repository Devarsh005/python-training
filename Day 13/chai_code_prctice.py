# score = 190
# if score>=101:
#     print('enter your score again')
#     exit()
# match score:
#     case x if 100>x>=90:
#         print('A')
#     case x if 89>=x>=80:
#         print('B')
#     case x if 79>=x>=70:
#         print('c')
#     case x if 69>=x>=60:
#         print('D')
#     case _:
#         print('F')

# import time
# attempt = 0
# max_try = 5
# wait_time = 1

# while attempt < max_try:
#     print("attempt",attempt,"wait time --",wait_time)
#     time.sleep(wait_time)
#     wait_time +=3
#     attempt +=1

# import math
# def area_circumference(radius):
#     area = math.pi * radius **2
#     circumference = 2 * math.pi * radius
#     return area , circumference

# # result = area_circumference(4)
# # print(f"area :{result[0]:.2f} circumferene : {result[1]:.2f}")

# a , c = area_circumference(4)
# print(f"area :{a:.3f} circumferene : {c:.2f}")

# def data(**kwargs):
#     print(kwargs.values())
#     print(kwargs.keys())
#     print(kwargs.items())
#     for key , value in kwargs.items():
#         print(key,value)
#     for x in zip(kwargs.keys(),kwargs.values()):
#         print(x)



# data(name ="Devarsh",age = 22 , college = "parul university" , qualification = "B.Tech IT")

# def generator(number):
#     for i in range(2,number,2):
#         yield i
# for num in generator(10):
#     print(num)

# def factorial(number):
#     if number ==1:
#         return 1
#     return number * factorial(number-1)
#     # while number > 1:
#     #     return number * factorial(number-1)
#     #     number-=1
    
# print(factorial(3))

import math
class Shape:
    def area(self):
        pass
    def perimeter(self,*args):
        return sum(args)
class circles(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius**2
    def perimeter(self):
        return 2*math.pi*self.radius
class square():
    def __init__(self,length):
        self.length = length
    def area(self):
        return self.length**2
objc = square(3)
print(objc.perimeter())