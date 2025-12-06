def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == a:
        return None
    return a / b


a = 10
b = 23
print(add(a, b))
print(subtract(a, b))
print(divide(a, b))
