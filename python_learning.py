def add(a, b, c, d):
    return a + b + c +d


def subtract(a, b, c, d):
    return a - b - c - d


def multiply(a, b, c, d):
    return a * b * c * d


def divide(a, b):
    if b == a:
        return None
    return a / b


a = 15
b = 59
c = 10
d = 22
print(add(a, b))
print(subtract(a, b))
print(divide(a, b))
