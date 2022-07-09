# 1.	Write a Python program to print "Hello Python"?
# def helloFunction():
#     print("Hello Python")
#
#
# helloFunction()


# 2.	Write a Python program to do arithmetical operations addition and division.?


# class ArithmeticFunc:
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def add(self, a, b):
#         print(self.a + self.b)
#
#     def subtract(self, a, b):
#         print(self.a - self.b)
#
#
# # instantiate
# obj1 = ArithmeticFunc(50, 100)
# obj2 = ArithmeticFunc(50, 30)
# obj1.add(0, 0)
# # call to methods
# # obj1.add(10, 10)
# obj2.subtract(0, 0)

# 3.	Write a Python program to find the area of a triangle?
def area_triangle():
    a = float(input("first arm length\n"))
    b = float(input("second arm length\n"))
    c = float(input("third arm length\n"))
    # calculate semi parameter
    s = (a + b + c) / 2
    # calculate area
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print(f'the area of triangle is %0.5f', area)


area_triangle()


# area_triangle(4, 5, 6)

# class TriangleArea:
#     try:
#         a = float(input("first arm length\n"))
#         b = float(input("second arm length\n"))
#         c = float(input("third arm length\n"))
#
#         def __init__(self, a, b, c):
#             self.a = a
#             self.b = b
#             self.c = c
#
#         def triangleArea(self):
#             # calculate semi parameter
#             s = (self.a + self.b + self.c) / 2
#             # calculate area
#             area = (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
#             print('area of triangle is %0.5f', area)
#             return
#     except BaseException:
#         print("input numeric only")
#
#     finally:
#         print(input("input any key for exit"))
#         exit()
#
#
# obj1 = TriangleArea()
# obj1.triangleArea()
# 4.Write a Python program to swap two variables?

# def swapFunc():
#     # To take inputs from the user
#     x = input('Enter value of x: ')
#     y = input('Enter value of y: ')
#     # create a temporary variable and swap the values
#     temp = x
#     x = y
#     y = temp
#
#     print('The value of x after swapping: {}'.format(x))
#     print('The value of y after swapping: {}'.format(y))


# swapFunc()

# 5.	Write a Python program to generate a random number?
# import random
#
#
# class Rand:
#     try:
#         x = int(input("press any number for continue \n"))
#         if x:
#             def generateFunction():
#                 x = random.randint(1, 100)
#                 # x = ['h', 'o', 'p', 'e']
#                 c1 = x
#                 cont = [x]
#                 # c1 = random.choice(x)
#                 # cont.append(c1)
#                 print(c1)
#                 print(f"generated number in list is", cont)
#                 return
#
#     except BaseException as e:
#         print(e.__class__)
#         # input("press any key for exit")
#         # exit()
#     finally:
#         input("press any key for exit \n")
#         exit()
#         print("code execution done")
#     generateFunction()
