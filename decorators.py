# Простой пример

# def decorator(foo):
#     def wrapper():
#         print("text before foo call")
#         foo()
#         print("text after foo call")
#     return wrapper

# def greet():
#     print("foo call")

# test_call = decorator(greet)

# test_call()

# @decorator
# def greet():
#     print("foo call")


# greet()

# Еще пример декоратора

# def each_pheasant(foo):
#     def wrapper():
#         print('каждый')
#         foo()
#         print('фазан')
#     return wrapper

# def hunter_is_sitting(foo):
#     def wrapper():
#         print('охотник')
#         foo()
#         print('сидит')
#     return wrapper

# def wishes_where(foo):
#     def wrapper():
#         print('желает')
#         foo()
#         print('где')
#     return wrapper

# def know():
#     print('знать')

# know = each_pheasant(hunter_is_sitting(wishes_where(know)))
# know()

# @each_pheasant
# @hunter_is_sitting
# @wishes_where
# def know():
#     print('знать')

# know()

# Декоратор с урока, для отслеживания времени выполнения функции

from time import time


def timer(function):
    def decorator(*args, **kwargs):
        start_time = time()

        function(*args, **kwargs)

        return (time() - start_time)
    
    return decorator

# @timer
# def count_100000000():
#     count = 0

#     for i in range(100000000):
#         count += 1
    
#     print(count)


# count_100000000()


# @timer
# def count_10000000_times_k(k):
#     count = 0

#     for i in range(10000000):
#         count += 1
    
#     print(k * count)

# count_10000000_times_k(3)

def cashe():
    args_list = []
    result_dict = {}

    def inner(foo):
        def wrapper(arg):
            if arg not in result_dict:
                args_list.append(arg)
                new_value = foo(arg)
                result_dict[arg] = new_value
            print(args_list)
            return result_dict[arg]
        return wrapper
    return inner


@timer
@cashe()
def power_two(k):
    return 2 ** k

print(power_two(20000000))
print(power_two(20000000))
print(power_two(3))
