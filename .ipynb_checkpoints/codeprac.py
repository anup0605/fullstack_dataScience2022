# add all digits
def addDigits(n):
    sum = 0
    while n != 0:
        sum = sum + n % 10
        n = n // 10
        print(sum)
    return sum


addDigits(243)
