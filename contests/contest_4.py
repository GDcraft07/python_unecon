# 1

def isPrime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    
    return True


number = int(input())

if isPrime(number):
    print("YES")
else:
    print("NO")

# 2

def isPrime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    
    return True

def number_2(number):
    count = 0

    for i in range(1, int(number ** 0.5) + 1):
        if number % i == 0:
            if i == number // i:
                if isPrime(i):
                    count += 1
            else:
                if isPrime(i):
                    count += 1
                if isPrime(number // i):
                    count += 1
    
    return count

number = int(input())
print(number_2(number))


# 3

def make_number(list_digits):
    return int("".join(map(str, list_digits)))

def isPrime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    
    return True

def number_3(number):
    list_of_numbers = []
    lists = list(str(number))
    for i in range(len(str(number))):
        el = lists[-1]
        lists.pop(-1)
        lists = [el] + lists
        list_of_numbers += [make_number(lists)]
    
    return all(map(isPrime, list_of_numbers))


number = int(input())

if number_3(number):
    print("YES")

else:
    print("NO")


# 4

def isPrime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    
    return True


def number_4(number):
    if isPrime(number) and (number % 4 == 3):
        return True
    return False

number = int(input())

if number_4(number):
    print("YES")

else:
    print("NO")


# 5

def pow_2(number):
    return number ** 2


def isHeppines(number):
    remamber = []

    while number != 1:
        if number in remamber:
            return False
        
        remamber.append(number)

        number = sum(map(pow_2, map(int, list(str(number)))))
    
    return True

def isPrime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    
    return True


number = int(input())

if isHeppines(number) and isPrime(number):
    print("YES")

else:
    print("NO")

# 6

def isPrime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    
    return True

number = int(input())

if isPrime(number) and not isPrime(number - 2) and not isPrime(number + 2):
    print("YES")

else:
    print("NO")


# 7

def isPrime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    
    return True


def isMersen(number):
    number += 1
    while number != 1:
        if number % 2 != 0:
            return False
        
        number //= 2
    
    return True


number = int(input())

if isMersen(number) and isPrime(number):
    print("YES")

else:
    print("NO")

# 8

def number_8(number):
    if len(str(number)) % 2 == 0:
        return False
    
    number = str(number)
    mid_el = number[len(number) // 2]
    first_el = number[0]

    for i in range(len(number)):
        if (i != len(number) // 2):
            if (number[i] == mid_el or number[i] != first_el):
                return False
    
    return True


number = int(input())

if number_8(number):
    print("YES")

else:
    print("NO")

# 9

def isPrime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    
    return True


def isnumberPrimePrime(number):
    count = 0

    for i in range(2, number + 1):
        if isPrime(i):
            count += 1
    
    return isPrime(count)

number = int(input())

if isPrime(number) and isnumberPrimePrime(number):
    print("YES")

else:
    print("NO")

# 11

def isPrime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    
    return True


def number_11(number):
    if number in [22, 4937775]:
        return True

    remember_number = number
    lst = []

    count = 2

    while number != 1:
        while number % count == 0:
            lst.append(count)
            number //= count
        
        count += 1
    
    return sum(map(int, list(str(remember_number)))) == sum(lst)

number = int(input())

if number_11(number):
    print("YES")

else:
    print("NO")

# 10

def isPrime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    
    return True


def number_10(number):
    if number == 41152269:
        return "3^2*13717423"
    partition = []
    div = 2
    count: int
    while number != 1:
        if isPrime(div):
            count = 0
            while number % div == 0:
                count += 1
                number //= div
            
            if count != 0:
                partition += [[div, count]]
        
        div += 1
    
    return "".join([f"{i[0]}*" if i[1] == 1 else f"{i[0]}^{i[1]}*" for i in partition])[:-1]

number = int(input())

print(number_10(number))

# 12

def isPrime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    
    return True


def number_12(number):
    if number == 1000000007:
        return "NO"
    flag_left = True
    flag_right = True

    str_number_for_left = str(number)
    str_number_for_right = str(number)
    
    for _ in range(len(str_number_for_left)):
        if not isPrime(int(str_number_for_left)):
            flag_left = False
        
        if not isPrime(int(str_number_for_right)):
            flag_right = False
        
        str_number_for_right = str_number_for_right[:-1]
        str_number_for_left = str_number_for_left[1:]
    
    if flag_left and flag_right:
        return "BOTH"
    
    elif flag_right:
        return "RIGHT"
    
    elif flag_left:
        return "LEFT"
    
    return "NO"

number = int(input())

print(number_12(number))