# 1.	Write a Python program to convert kilometers to miles?
# kilometers = float(input("Enter value of kilometer\n"))
# conversion_factor = 0.621371
# miles = kilometers * conversion_factor
# print(f"%0.2f kilometers is equal to %0.2f miles" % (kilometers, miles))

# 2.	Write a Python program to convert Celsius to Fahrenheit?
# Celsius = float(input("Enter value of Celsius Degree\n"))
# Fahrenheit = (Celsius * 1.8) + 32
# print(f"%0.1f degree Celsius is equal to %0.1f Fahrenheit" % (Celsius, Fahrenheit))

# 3.	Write a Python program to display calendar?
# import calendar
#
# yy = int(input("Enter year: yyyy format\n"))
# mm = int(input("Enter month mm format\n"))
# print(calendar.month(yy, mm))
# 4.	Write a Python program to solve quadratic equation?
# ax2 + bx + c = 0, where
# a, b and c are real numbers and a ≠ 0
# import cmath
#
# a = int(input(f"Enter real value of a\n"))
# b = int(input(f"Enter real value of b\n"))
# c = int(input(f"Enter real value of c\n"))
# # the discriminant value of equation
# D = (b ** 2) - (4 * a * c)
# # solution of quadratic equation
# result1 = (-b - cmath.sqrt(D)) / (2 * a)
# result2 = (-b + cmath.sqrt(D)) / (2 * a)
# print('Solution of equation are {0} & {1}'.format(result1, result2))

# 5.	Write a Python program to swap two variables without temp variable?

x = int(input("enter numeric first value\n"))
y = int(input("enter numeric second value\n"))
print('input value of x={0}, y={1}'.format(x, y))
x ^= y
y ^= x
x ^= y
print('output value of x={0}, y={1}'.format(x, y))
