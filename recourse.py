# Глубокий анализ стека вызовов
def trace_recursion(func):
    """Декоратор для трассировки рекурсивных вызовов"""
    depth = 0
    
    def wrapper(*args, **kwargs):
        nonlocal depth
        indent = "    " * depth
        print(f"{indent}→ {func.__name__}({args[0]})")
        depth += 1
        result = func(*args, **kwargs)
        depth -= 1
        print(f"{indent}← {func.__name__} → {result}")
        return result
    
    return wrapper

@trace_recursion
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


@trace_recursion
def factorial(n):
    """Классическая рекурсия с линейной глубиной"""
    if n < 0:
        raise ValueError("Факториал отрицательного числа не определен")
    if n <= 1:
        return 1
    return n * factorial(n - 1)



class MemoizedRecursion:
    def __init__(self):
        self.cache = {}
    
    def fibonacci(self, n):
        if n in self.cache:
            return self.cache[n]
        
        if n <= 1:
            result = n
        else:
            print(n)
            result = self.fibonacci(n - 1) + self.fibonacci(n - 2)
        
        self.cache[n] = result
        return result


# print(MemoizedRecursion().fibonacci(10))



class MyMemoizedRecourse:
    def __init__(self):
        self.memory = {}
    

    def my_recourse(self, n):
        if n in self.memory:
            return self.memory[n]
        
        if n <= 1:
            return 1
        
        result = self.my_recourse(n - 1) + self.my_recourse(n - 2)


def calc(n):
    if n <= 0:
        return
    
    print(n)
    calc(n - 1)

def rcalc(n):
    if n == 0:
        return
    
    rcalc(n - 1)
    print(n)

# calc(3)
# rcalc(3)


def sm(x):
    if x == 0:
        return 0
    return sm(x // 10) + x % 10

# print(sm(123))

# прямой ход
def reverse(line):
    if not line:
        return ""
    
    return line[-1] + reverse(line[:-1]) 

# print(reverse("abc"))

# обратный ход
def new_reverse(line):
    if not line:
        return ""
    
    return new_reverse(line[1:]) + line[0]

# print(new_reverse("abc"))


# прямой ход

def modi(number, div=1, result=[]):
    if number < div * div:
        return sorted(result)
    
    if number == div * div:
        result += [div]

    elif number % div == 0:
        result += [div, number // div]
    

# print(modi(6))

# обратный ход

def new_modi(number, div=1):
    if div > number:
        return []
    
    rest = new_modi(number)

    if number % div == 0:
        return [div] + rest
    
    return rest


# прямой ход
def isPrime(number, div=2):
    if number < 2:
        return False
    
    if number < div * div:
        return True
    
    if number % div == 0:
        return False
    
    return isPrime(number, div + 1)


# print(isPrime(1))

def isEven(n):
    if n == 0:
        return True
    
    return isOdd(n - 1)


def isOdd(n):
    if n == 1:
        return False
    
    return isEven(n - 1)


def myCacheDeco(funk):
    memory = {}

    def doFunk(n):
        nonlocal memory
        if n not in memory:
            memory[n] = funk(n)
            print(memory[n])
        
        return memory[n]
    
    return doFunk


@myCacheDeco
def fibonachi_1(n):
    if n <= 1:
        return n
    
    return fibonachi_1(n - 1) + fibonachi_1(n - 2)

print(fibonachi_1(6))


def dept(lists):
    if not isinstance(lists, list):
        return 0
    
    mx = 0

    for element in lists:
        k = dept(element)
        if k > mx:
            mx = k
        
    return 1 + mx

# print(dept([12, [12, [12]]]))


def r_map(funk, seq):
    if not seq:
        return []
    
    return [funk(seq[0])] + r_map(funk, seq[1:])


"""
камень - 1
ножницы - 2
бумага - 3

1 - 2
2 - 3
3 - 1

"""