# 1.	Write a Python Program to Display Fibonacci Sequence Using Recursion?
# def recFibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return recFibonacci(n - 1) + recFibonacci(n - 2)
#
#
# nterms = int(input("Enter number of fibonacci sequence\n"))
# # check if the number of terms is valid
# if nterms <= 0:
#     print("enter positive integer only")
# else:
#     print("Fibonacci Sequence")
#     for i in range(nterms):
#         print((recFibonacci(i)))

# 2.	Write a Python Program to Find Factorial of Number Using Recursion?
# def recur_factorial(num):
#     if num == 1:
#         return num
#     else:
#         return num * recur_factorial(num - 1)
#
#
# inpNum = int(input("Enter valid Number only"))
# if inpNum < 0:
#     print("does not exit for negative integer")
# elif inpNum == 0:
#     print("The factorial of 0 is 1")
# else:
#     print("the factorial of", inpNum, "is", recur_factorial(inpNum))

# 3.	Write a Python Program to calculate your Body Mass Index?
# height = float(input("input height in feet\n"))
# weight = float(input("input weight value in kilogram\n"))
# print("Body mass index is:", round(weight / (height * height), 2))


# 4.	Write a Python Program to calculate the natural logarithm of any number?
# import math
#
# intNum = float(input("Enter number for log value\n"))
# print("log value", math.log(intNum))

# 5.	Write a Python Program for cube sum of first n natural numbers?

# Returns the sum of series
def sumOfSeries(n):
    # sum = 0
    # for i in range(1, n + 1):
    #     sum += i * i * i
    #
    # return sum

    x = (n * (n + 1) / 2)
    return int(x * x)


# Driver Function
n = int(input("Enter natural numbers to find sum of series \n"))
print(sumOfSeries(n))
