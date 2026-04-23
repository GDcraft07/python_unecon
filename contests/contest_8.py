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
        yield f"{number + 1}: {line}"


# 6

def filter_numbers(numbers, condition):
    for number in numbers:
        if condition(number):
            yield number


# 7

def cycle(items):
    index = 0

    while True:
        yield items[index]

        index += 1
        if index == len(items):
            index = 0


# 8

def isPrime(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    
    return True

def primes():
    prime = 2

    while True:
        yield prime

        prime += 1

        while not isPrime(prime):
            prime += 1


# 9

def range_with_step(start, stop, step):
    while start < stop:
        yield start
        start += step


# 10

def chain(*iterables):
    for iterator in iterables:
        for item in iterator:
            yield item


# 11

def take_n(iterator, n):
    for i in range(n):
        try:
            yield next(iterator)

        except StopIteration:
            return None


# 12

def flatten(nested_list):
    for el in nested_list:
        if type(el) is list:
            yield from flatten(el)
        else:
            yield el
        