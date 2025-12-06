def add(a, b, c):
    return a + b + c


def subtract(a, b, c):
    return a - b - c


def multiply(a, b, c):
    return a * b * c


def divide(a, b):
    if b == a:
        return None
    return a / b


a = 15
b = 59
c = 10
print(add(a, b))
print(subtract(a, b))
print(divide(a, b))
