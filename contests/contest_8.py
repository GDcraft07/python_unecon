# 1

def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i


# 2

def counter(start=0):
    while True:
        yield start
        start += 1


# 3

def fibonacci():
    first = 0
    second = 1

    while True:
        yield first
        first, second = second, first + second


# 4

def powers_of_two(n):
    for i in range(0, n + 1):
        yield 2 ** i


# 5

def read_lines(lines):
    for number, line in enumerate(lines):
        yield f"{number}:{line}"


print(list(read_lines(["12", "12", "124"])))