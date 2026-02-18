# 1

def isBigYear(year):
    if (year % 100 != 0 and year % 4 == 0) or (year % 400 == 0):
        return "YES"
    return "NO"

year = int(input())
print(isBigYear(year))

# 2

def isAccess(age, money, flag_value):
    flag: bool
    if flag_value == "yes":
        flag = True
    else:
        flag = False
    
    if flag or (age < 18 or age > 60) or (money < 30000):
        return "Denied"
    
    return "Access"


age = int(input())
money = int(input())
flag_value = input()

print(isAccess(age, money, flag_value))

# 3

def gcd(a, b):
    if a < b:
        a, b == b, a
    
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    
    return a + b


a = int(input())
b = int(input())

print(gcd(a, b))

# 4

def sum_digits(number):
    if number < 10:
        return number
    
    return sum_digits(sum(map(int, list(str(number)))))


number = int(input())

print(sum_digits(number))

# 5

def count_steps(number, count=0):
    if number == 1:
        return count
    
    if number % 2 == 0:
        return count_steps(number // 2, count + 1)
    return count_steps(3 * number + 1, count + 1)

number = int(input())

print(count_steps(number))

# 6

def isPalendrom(word):
    word = word.replace(" ", "").lower()

    return word == word[::-1]

word = input()

print(isPalendrom(word))

# 7

def isStrongPassword(password):
    list_password = list(password)
    flags_digit = list(map(lambda x: x.isdigit(), list_password))
    flags_upper = list(map(lambda x: x.isupper(), list_password))

    if len(list_password) >= 8 and any(flags_digit) and any(flags_upper):
        return "Strong"
    return "Weak"


password = input()

print(isStrongPassword(password))

# 8

def normalPhone(number):
    return f"+7 ({number[1:4]}) {number[4:7]}-{number[7:9]}-{number[9:]}"

number = input()

print(normalPhone(number))

# 9

def perfectNumber(number):
    list_divider = [1]

    for i in range(2, int(number ** 0.5) + 1):
        if i * i == number:
            list_divider.append(i)
        elif number % i == 0:
            list_divider.append(i)
            list_divider.append(number // i)
    
    if sum(list_divider) == number:
        return "YES"
    return "NO"


number = int(input())

print(perfectNumber(number))

# 10

def archi(text):
    result_text = ""
    current_letter = text[0]
    count = 1
    for i in range(1, len(text)):
        if current_letter == text[i]:
            count += 1
        else:
            result_text += f"{current_letter}{count}"
            current_letter = text[i]
            count = 1
    
    result_text += f"{current_letter}{count}"

    return result_text


text = input()
print(archi(text))

# 12

def isPrime(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


def allPrime(number):
    answer_list = []
    for i in range(2, number + 1):
        if isPrime(i):
            answer_list.append(i)
    
    return " ".join(map(str, answer_list))


number = int(input())

print(allPrime(number))

# 11

def isValid(line):
    current_sum = 0

    for i in range(0, len(line)):
        if i % 2 == 0:
            digit = 2 * int(line[i])
            if digit > 9:
                digit -= 9
            current_sum += digit
        else:
            current_sum += int(line[i])
    if current_sum % 10 == 0:
        return "Valid"
    return "Invalid"

line = input()

print(isValid(line))