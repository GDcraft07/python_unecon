# 1

def safe_divide(a, b):
    try:
        return a / b
    
    except ZeroDivisionError:
        return "Деление на ноль"
    
    except TypeError:
        return "Ошибка типов"


# 2

def to_int(value):
    try:
        return int(value)
    
    except:
        return None


# 3

def get_element(lst, index, default=None):
    try:
        return lst[index]
    
    except IndexError:
        return default

# 4

def get_key(d, key, default=None):
    try:
        if type(d) is dict:
            return d[key]
        return default
    
    except KeyError:
        return default
    
    except TypeError:
        return default

# 5

def process_with_log(value, processor):
    print("Начало обработки")

    try:
        return processor(value)
    
    finally:
        print("Конец обработки")


# 6

def process_data(data):
    res = []
    
    for item in data:
        if type(item) is int:
            res += [item * 2]
        elif type(item) is str:
            res += [item.upper()]
        elif type(item) is list:
            res += [len(item)]
        else:
            raise TypeError(f"Неподдерживаемый тип: {type(item).__name__}")
    
    return res


# 7

def retry(func, max_attempts=3):
    remember_error = ""

    for _ in range(max_attempts):
        try:
            return func()
        except Exception as e:
            remember_error = e
        
    return f"Провал: {remember_error}"

# 8

def calc(a, b, op):
    if op not in "+-*/":
        raise ValueError("Неизвестная операция")
    
    try:
        return eval(f"{a}{op}{b}")
    
    except ZeroDivisionError:
        return "Деление на ноль"


# 9

def input_number(prompt):
    while 1:
        try:
            out = input(prompt)
            return float(out)
        
        except ValueError:
            print("Ошибка, попробуйте еще")

# 10

def deep_operation(data):
    if not data:
        return 0
    
    if type(data[0]) is list:
        return deep_operation(data[0]) + deep_operation(data[1:])
    
    if type(data[0]) is int or type(data[0]) is float:
        return data[0] + deep_operation(data[1:])
    
    else:
        raise TypeError("Обнаружены нечисловые данные")

# 11

def safe_execute(func, default=None):
    try:
        return func()
    
    except:
        try:
            if type(default) is type(lambda:0):
                return default()
            
            return default
        
        except:
            return None

# 12

def parse_data(data):
    try:
        return [int(i.strip()) for i in data.split(",")]
    
    except ValueError as error:
        raise ValueError("Ошибка парсинга") from error
