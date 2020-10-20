def fibonacci(n):
    a = 0
    b = 1

    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2,n):
            value = a + b
            a = b
            b = value
        return value
    
print(fibonacci(10))
# 55
            
            