def fibonacci(n):
    a, b = 0, 1
    if n < 0:
        print("incorrect input")
        return
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for _ in range(2, n + 1):
            c = a + b
            a = b
            b = c
        return b
print(fibonacci(5)) 
print(fibonacci(10)) 
