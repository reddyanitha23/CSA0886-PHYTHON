def convertToBase7(num):
    if num == 0:
        return "0"
    negative = '-' if num < 0 else ''
    num = abs(num)
    base7 = ''
    while num:
        base7 = str(num % 7) + base7
        num //= 7
    return negative + base7
num1 = 100
print(convertToBase7(num1))

