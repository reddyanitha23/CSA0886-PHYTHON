def isPerfectNumber(num):
    if num <= 1:
        return False
    sum_divisors = 1
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            sum_divisors += i + (num // i if i != num // i else 0)
    return sum_divisors == num

# Test Case 1
num1 = 28
print(isPerfectNumber(num1))



