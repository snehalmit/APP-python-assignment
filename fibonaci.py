def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))

a = 6
b = 1

for i in range(5):
    print(a, end=" ")
    c = a + b
    a = b
    b = c