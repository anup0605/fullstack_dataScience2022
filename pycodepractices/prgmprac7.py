# 1.	Write a Python Program to find sum of array?
# def findSumOfArrays():
#     try:
#         my_list = []
#
#         while True:
#             my_list.append(float(input("Enter number in array for calculate sum of array\n")))
#             sm = 0
#             for i in range(0, len(my_list)):
#                 sm = sm + my_list[i]
#             print("Sum of all the elements of an array: ", my_list)
#             print("Sum of all the elements of an array: " + str(sm))
#     # if the input is not number, just print the list
#     except Exception as err:
#         print("Error:", err)
#         print(my_list)
#
#
# findSumOfArrays()

# 2.	Write a Python Program to find largest element in an array?
# try:
#     def largest(arr, n):
#         ans = max(arr)
#         return ans
#
#
#     arr = [20, 50.74141, 7878, 5758, 1.0, 0.001]
#     n = len(arr)
#     print("Largest in given array ", largest(arr, n))
# except Exception as err:
#     print("Error", err)

# 3.	Write a Python Program for array rotation?
# slicing approach to rotate the array
# def rotateList(arr, d, n):
#     arr[:] = arr[d:n] + arr[0:d]
#     return arr
#
#
# # To test above function
# arr = [1, 22, 333, 4444, 55555, 666666, 7777777]
# print(arr)
# print("Rotated list is")
# print(rotateList(arr, 2, len(arr)))

# 4.	Write a Python Program to Split the array and add the first part to the end?
# def splitArray(arr, n, k):
#     # pass
#     for i in range(0, 3):
#         x = arr[0]
#         for j in range(0, n-1):
#             arr[j] = arr[j + 1]
#         arr[n-1] = x
#     print(arr[j], end=' ')
#
#
# # pass array for test
# arr = [15, 20, 25, 30, 35]
# n = len(arr)
# position = 0
# splitArray(arr, n, position)
# for i in range(0, n):
#     print(arr[i], end=' ')

# 5.	Write a Python Program to check if given array is Monotonic?
# check if monotone
# function definition
def ismonotone(a):
    n = len(a)  # size of array
    if n == 1:
        return True
    else:
        # check for monotone behaviour
        if all(a[i] >= a[i + 1] for i in range(0, n - 1) or a[i] <= a[i + 1] for i in range(0, n - 1)):
            return True
        else:
            return False


A = [6, 5, 4, 2]
print(ismonotone(A))
b = [6, 2, 4, 2]
print(ismonotone(b))
c = [4, 3, 2]
print(ismonotone(c))
d = [1]
print(ismonotone(d))
