# 1.	Write a Python Program to Find the Factorial of a Number?
# n = int(input("Enter number for Find the Factorial of a Number\n "))
# factorial = 1
# # check number for negative,positive & zero
# if n < 0:
#     print("factorial does not exist for negative numbers")
# elif n == 0:
#     print('factorial of 0 is 1')
# else:
#     for i in range(1, n + 1):
#         factorial = factorial * i
#     print("Factorial of", n, "is", factorial)

# 2.	Write a Python Program to Display the multiplication Table?
# try:
#     n = float(input("enter number for multiplication table\n"))
#     for i in range(1, 11):
#         if i >= 1:
#             # print("table of your input number is {0},".format(j * i))
#             print(n, '*', i, '=',(n * i)
# except BaseException as e:
#     print(str(e))

# 3.	Write a Python Program to Print the Fibonacci sequence?
# n = int(input("enter number for Fibonacci sequence"))
# a = 1
# b = 0
# print(b)
# print(a)
# for i in range(0, n):
#     while a < n:
#         c = b
#         b = a
#         a = c + b
#         print(a)

# 4.	Write a Python Program to Check Armstrong Number?
# 153
# 370
# 371
# 407
# 1634
#
n = int(input("any 4 digit number to check Armstrong Number\n"))
# to find for the power of number
order = len(str(n))
# initialization of sum
sum1 = 0
temp = n
# loop for check till positive or zero
while temp > 0:
    digit = temp % 10
    sum1 = sum1 + digit ** order
    # for return with int value as 0.0=0
    temp = temp // 10
    # print & check with valid number
if n == sum1:
    print(n, ",this number is a armstrong & last converted digit of n ={0}".format(temp))
else:
    print("this number not a armstrong number")

# 5.	Write a Python Program to Find Armstrong Number in an Interval?
#
# lower = int(input("enter lower limit to find Armstrong Number in an Interval"))
# upper = int(input("enter upper limit to find Armstrong Number in an Interval"))
#
# for num in range(lower, upper + 1):
#
#     # order of number
#     order = len(str(num))
#
#     # initialize sum
#     sum = 0
#
#     temp = num
#     while temp > 0:
#         digit = temp % 10
#         sum += digit ** order
#         temp //= 10
#
#     if num == sum:
#         print(num)

# 6.	Write a Python Program to Find the Sum of Natural Numbers?
# n1 = int(input("Enter a number"))
# if n1 < 0:
#     print("enter positive number only")
# else:
#     sum = 0
#     while n1 > 0:
#         sum = sum + n1
#         n1 = n1 - 1
#         # break
#     print("the sum is", sum)
