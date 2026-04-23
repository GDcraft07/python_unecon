# 1

def number_1(line, number):
    answer = [[] for _ in range(number)]

    for i in range(len(line)):
        answer[i % number].append(line[i])

    return answer


print(number_1(input().split(), int(input())))

# 2

def number_2(number):
    a, b, c = 1, 1, 1
    lst = []

    for _ in range(number):
        lst += [a]
        a, b, c = b, c, a + b + c
    
    return lst


print(" ".join(map(str, number_2(int(input())))))


# 3

def number_3(a, b, c):
    x0 = -b / (2 * a)
    y0 = (4 * a * c - (b ** 2)) / (4 * a)

    return f"({x0:.1f}, {y0:.1f})"

print(number_3(float(input()), float(input()), float(input())))


# 4

from itertools import permutations

def number_4(line):
    count = 0

    for i in set(permutations(line)):
        word = ''.join(i)
        
        if word.index('Г') > word.index('А') and word.index('Г') > word.index('И'):
            count += 1

    return count

print(number_4(input()))


# 5

from itertools import product

def number_5(line):
    all_digits = list(set(line))

    count = 0

    for i in product(all_digits, repeat=12):
        if "55" not in "".join(i) and i[0] != "0":
            count += 1
        
    return count


print(number_5(input()))


# 6

from itertools import product


def number_6(number_1, number_2):
    count_tail = 0

    for i in product(['И', 'Н', 'А'], repeat=(number_1 - 4)):
        if i.count('Н') >= number_2:
            count_tail += 1

    return 24 * count_tail


print(number_6(*map(int, input().split())))

# 7

def my_make_str(number):
    return str(number) if number != 0 else "0"

def number_7(number_1, number_2):
    return [i * number_2 for i in range(int(number_1))]

print(" ".join(map(my_make_str, number_7(*map(float, input().split())))))