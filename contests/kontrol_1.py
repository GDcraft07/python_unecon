# 1

def count_args(*args):
    return len(args)


args = input().split()

print(count_args(*args))

# 2

def sq_sum(*args):
    answer = 0

    for i in args:
        answer += (i ** 2)
    
    return answer


args = map(float, input().split())

print(sq_sum(*args))


# 3

def mean(*args):
    sums = 0
    count = 0
    for i in args:
        try:
            sums += float(i)
            count += 1
        except ValueError:
            pass
    
    if count:
        return sums / count
    return 0

args = input().split()

print(mean(*args))

# 4

numbers = list(map(int, input().split()))

count = 0

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j]:
            count += 1

print(count)

# 5

ip = list(map(int, input().split("."))); print("YES") if len(ip) == 4 and all(map(lambda x: 0 <= x <= 255, ip)) else print("NO")

# 6

print("NO") if "01" in "".join(map(lambda x: bin(int(x))[2:].zfill(8), input().split("."))) else print("YES")

# 7

big_then_zero = []
zeros = []

for i in range(int(input())):
    number = int(input())
    if number < 0:
        print(number)
    elif number == 0:
        zeros += [number]
    else:
        big_then_zero += [number]

print("\n".join(map(str, zeros)))

print("\n".join(map(str, big_then_zero)))

# 8

line = input().split("-"); print("YES") if (all(map(lambda x: all([i.isdigit() for i in x]), line)) and ((len(line) == 3 and len(line[0]) == 3 and len(line[1]) == 3 and len(line[2]) == 4)) or (len(line) == 4 and line[0] == "7" and len(line[1]) == 3 and len(line[2]) == 3 and len(line[3]) == 4)) else print("NO")

# 9

def isPrime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    
    return True

a, b = map(int, input().split()); print("\n".join(map(str, [i for i in range(a, b + 1) if isPrime(i)])))

# 10

def sqrt(number):
    if number < 10:
        return number
    
    return sqrt(sum(map(int, list(str(number)))))

print(sqrt(int(input())))