# 1

def power_factory(exp):
    def power(number):
        return number ** exp
    
    return power

# 2

def make_counter():
    count = 0

    def upper_count():
        nonlocal count
        count += 1
        return count

    return upper_count

# 3

def make_cached(f):
    cache = {}

    def do_function(arg):
        nonlocal cache
        if str(arg) in cache:
            return cache[str(arg)]
        
        cache[str(arg)] = f(arg)
        return cache[str(arg)]
    
    return do_function


# 4

def logger(function):
    def decorators(*args):
        print_args = ", ".join(map(str, args))
        print(f"Вызов: {function.__name__}, аргументы: ({print_args})")
        result = function(*args)
        print(f"Результат: {result}")
        return result
    return decorators


# 5
import time


def timer(function):
    def decorator(*args, **kargs):
        t1 = time.time()
        function_result = function(*args, **kargs)
        print(f"Выполнено за {time.time() - t1:.4f} сек")
        return function_result
    return decorator


# 6

def limit_calls(n):
    count = 0

    def inner(function):
        def wapper(*args, **kargs):
            nonlocal count
            count += 1

            if count > n:
                function_result = None
            else:
                function_result = function(*args, **kargs)
            
            return function_result
        return wapper
    return inner


# 7

def compose(f, g):
    def h(x):
        return f(g(x))
    return h


# 8

def partial(func, *fixed_args):
    def new_func(*new_args):
        return func(*fixed_args, *new_args)
    
    return new_func

# 9

def add_prefix(prefix):
    def inner(function):
        def wapper(*args, **kargs):
            return f"{prefix}{function(*args, **kargs)}"
        return wapper
    return inner


# 10

def make_accumulator():
    count = 0

    def make_funck(number):
        nonlocal count
        count += number
        return count
    return make_funck

# 11

def expect_types(a_type, b_type):
    def inner(function):
        def wapper(*args):
            for i in args:
                if not type(i) is a_type and not type(i) is b_type:
                    raise TypeError
            
            return function(*args)
        return wapper
    return inner


# 12

def make_functions(n):
    lst = []
    for i in range(n):
        lst.append(lambda x=i: x)
    return lst

funcs = make_functions(3)
print([f() for f in funcs])

funcs = make_functions(5)
print([f() for f in funcs[2:5]])
