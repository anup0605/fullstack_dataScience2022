# 1.	Write a Python Program to Check if a Number is Positive, Negative or Zero?
# n1 = float(input("Enter a Number is Positive, Negative or Zero\n"))
# if n1 > 0 and n1 != 0:
#     print("entered number is positive", n1)
# elif n1 == 0:
#     print("entered number is zero")
# else:
#     print("entered number is negative")

# 2.	Write a Python Program to Check if a Number is Odd or Even?
# try:
#     n = int(input("Enter any Odd or Even number\n"))
#     if n/2 and n % 2 == 0:
#         print('entered number={0} is Even'.format(n))
#     else:
#         print("Enter Odd number is {0}".format(n))
# except BaseException as e:
#     print("input valid number only,error is {0}".format(e))
# finally:
#     print("your entered number is {0}".format(n))

# 3.	Write a Python Program to Check Leap Year?

# try:
#     n = int(input("To check Leap Year,Enter year in format yyyy\n"))
#     if n % 400 == 0 and n % 100 == 0:
#         print('entered Year={0} is Leap Year '.format(n))
#     elif n % 4 == 0 and n % 100 != 0:
#         print('entered Year {0} is Leap Year '.format(n))
#     else:
#         print("Entered year {0} is not Leap year".format(n))
#
# except BaseException as e:
#     print("input valid number only,error is {0}".format(e))
# finally:
#     print("your entered year is {0}".format(n))

# 4.	Write a Python Program to Check Prime Number?
# try:
#     n = int(input("enter any number to check prime or not\n"))
#     if n > 1 and n % 2 == 0:
#         print("entered number {0} is prime".format(n))
#     elif n < 1:
#         print("entered number {0} is not prime".format(n))
#     else:
#         print("this is not prime number & check with exception")
# except BaseException as e:
#     print(e.__class__)
#     print(str(e))
# finally:
#     print("keep input valid number only")


# 5.	Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?
# To take input from the user
num = int(input("Enter a number: "))

# define a flag variable
flag = False

# prime numbers are greater than 1
if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

# check if flag is True
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")
