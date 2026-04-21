# 1

def factorial(number):
    return 1 if number <= 1 else number * factorial(number - 1)


# 2

def sum_digits(number):
    if number <= 9:
        return number
    
    return number % 10 + sum_digits(number // 10)


# 3

def power(a, n):
    if n == 0:
        return 1
    
    if n == 1:
        return a
    
    return a * power(a, n - 1)


# 4

def cashe():
    args_list = []
    result_dict = {}

    def inner(foo):
        def wrapper(arg):
            if arg not in result_dict:
                args_list.append(arg)
                new_value = foo(arg)
                result_dict[arg] = new_value
            return result_dict[arg]
        return wrapper
    return inner

@cashe()
def fibonacci(number):
    if 1 <= number <= 2:
        return 1
    
    if number == 0:
        return 0
    
    return fibonacci(number - 1) + fibonacci(number - 2)

# 5

def is_palindrome(line):
    if len(line) <= 1:
        return True
    
    if line[0] != line[-1]:
        return False
    
    return is_palindrome(line[1:-1])


# 6

def reverse_string(line):
    if len(line) == 0:
        return ""
    
    return reverse_string(line[1:]) + line[0]


# 7

def binary_search(arr, target, left, right):
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    
    elif target < arr[mid]:
        return binary_search(arr, target, left, mid - 1)
    
    return binary_search(arr, target, mid + 1, right)



# 8

def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk from {source} to {target}")
    
    else:
        hanoi(n - 1, source, target, auxiliary)
        print(f"Move disk from {source} to {target}")
        hanoi(n - 1, auxiliary, target, auxiliary)

# 9

def nested_sum(lst):
    if not lst:
        return 0
    
    if type(lst[0]) is list:
        return nested_sum(lst[0]) + nested_sum(lst[1:])
    
    return lst[0] + nested_sum(lst[1:])

# 10

def count_occurrences(lst, target):
    if not lst:
        return 0
    
    if type(lst[0]) is list:
        return count_occurrences(lst[0], target) + count_occurrences(lst[1:], target)
    
    if lst[0] == target:
        return 1 + count_occurrences(lst[1:], target)
    return count_occurrences(lst[1:], target)

# 11

def gcd(number_1, number_2):
    if number_2 > number_1:
        number_1, number_2 = number_2, number_1
    
    if number_2 == 0:
        return number_1
    
    return gcd(number_2, number_1 % number_2)


# 12

def substrings(line):
    if len(line) == 0:
        return []
    
    if len(line) == 1:
        return [line]
    
    result = substrings(line[:-1])
    
    for i in range(len(line)):
        result += [line[i:]]
    
    return result

