try:
    print(5 / 0)
except:
    print("Иди нахуй")


# ValueError ZeroDivisionError TypeError IndexError KeyError FileNotFoundError ImportError

# Хуевый тон кода

try:
    a = int(input())
    print(5 / a)

except ValueError:
    print("Неверный ввод")

except ZeroDivisionError:
    print("Не делим на ноль")

except:
    print("Иди нахуй")

else:
    print("ГГ ВП ВСЕ РАБОТАЕТ")


# Привльный тон кода

try:
    a = int(input())

except ValueError or TypeError:
    print(f"Долбаеб введи число")


else:
    try:
        print(5 / a)
    
    except:
        print("Долби нах ты на нуль делишь")


# Про raise

def f(x):
    if x < 0:
        raise Exception
    return x

print(f(-1))