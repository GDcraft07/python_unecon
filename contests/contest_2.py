# 1

def number_1(line: str):
    line = line.replace("A", "0")
    line = line.replace("B", "0")
    line = line.replace("C", "1")
    line = line.replace("\"", "0")

    return max(map(len, line.split("0")))

line = input()
print(number_1(line))

# 2

from collections import defaultdict

def number_2(line):
    letter_dict = defaultdict(int)
    current_letter = line[0]
    count = 0

    for i in range(0, len(line)):
        if current_letter == line[i]:
            count += 1
        else:
            current_letter = line[i]
            count = 1
        if count > letter_dict[line[i]]:
                letter_dict[line[i]] = count
    answer = ""
    max_number = 0
    for i in letter_dict:
         if max_number < letter_dict[i]:
              max_number = letter_dict[i]
    
    for i in letter_dict:
         if letter_dict[i] == max_number:
              answer += i
    
    return (max_number, answer)

line = input()

answer = number_2(line)

for i in range(len(answer[1])):
     print(f'{answer[1][i]} {answer[0]}')

# 3

def number_3(line: str):
    min_odd_number = -1
    flag: bool
    count = ""

    if line[0].isdigit():
        flag = False
    else:
        flag = True

    for i in range(len(line)):
        if line[i].isdigit():
            if flag:
                count += line[i]
        
        else:
            if not flag:
                flag = True
            else:
                if count != "":
                    if int(count) % 2 != 0 and (min_odd_number == -1 or min_odd_number > int(count)) and count[0] != "0":
                        min_odd_number = int(count)
                    count = ""
    
    return min_odd_number

line = input()

print(number_3(line))

# 14

def number_14(line, sub_line):
    line = line.lower()
    sub_line = sub_line.lower()
    if len(sub_line) > len(line):
        sub_line, line = line, sub_line
    
    if sub_line in line:
        return "Да"
    return "Нет"

line = input()
sub_line = input()

print(number_14(line, sub_line))

# 13

from collections import defaultdict


def make_defaultdict(line):
    letter_dict = defaultdict(int)

    for i in line:
        letter_dict[i] += 1
    
    return letter_dict


def number_13(line_1, line_2):
    letter_dict_1 = make_defaultdict(line_1.lower())
    letter_dict_2 = make_defaultdict(line_2.lower())

    flag = False

    if len(line_1) == len(line_2):
        flag = True

        for i in letter_dict_1:
            if letter_dict_1[i] != letter_dict_2[i]:
                flag = False
    
    return "Да" if flag else "Нет"


line_1 = input()
line_2 = input()

print(number_13(line_1, line_2))

# 12

def number_12(line):
    count = 0

    for i in "bcdfghklmnpqrstvxz":
        count += line.lower().count(i)
    
    return count

line = input()

print(number_12(line))

# 11

def number_11(line):
    answer = ""

    for i in line:
        if i.isdigit() or i.isalpha() or (i == " " and answer[-1] != " "):
            answer += i
    
    return answer

line = input()

print(number_11(line))

# 10

def number_10(line):
    line = ''.join(line.lower().split())
    new_line = ""

    for i in line:
        if i.isdigit() or i.isalpha():
            new_line += i
    
    new_line = new_line.replace("й", "и")
    new_line = new_line.replace("ё", "е")

    return "Да" if new_line == new_line[::-1] else "Нет"

line = input()

print(number_10(line))

# 8

def number_8(line):
    massive_without_dot = line.split(".")

    for i in range(len(massive_without_dot)):
        if massive_without_dot[i].count("A") < 3:
            massive_without_dot[i] = ""
    
    return max(map(len, massive_without_dot))

line = input()

print(number_8(line))

# 7

def number_7(line):
    massive_without_dot = list(map(len, line.split(".")))
    if len(massive_without_dot) <= 4:
        return sum(massive_without_dot) + len(massive_without_dot) - 1
    
    summa = sum(massive_without_dot[:4]) + 3
    index = 0
    for i in range(4, len(massive_without_dot)):
        if summa + massive_without_dot[i] - massive_without_dot[index] > summa:
            summa = summa + massive_without_dot[i] - massive_without_dot[index]
        index += 1
    
    return summa

line = input()

print(number_7(line))

# 6

def number_6(line):
    massive_without_qw = line.split("QW")

    ans = max(map(len, massive_without_qw))
    return ans if len(massive_without_qw) == 1 else ans + 1

line = input()

print(number_6(line))

# 4

def number_4(line):
    count = 0
    flag = -1
    check = 0
    answer = 1

    for i in range(1, len(line)):
        if line[i - 1] < line[i]:
            count += 1
            if flag == -1:
                flag = i
        else:
            if count > check:
                check = count
                answer = flag
            flag = -1
            count = 0
    if count > check:
        answer = flag
    
    return answer

line = input()

print(number_4(line))

# 9

def number_9(line):
    line = line.strip()

    answer = 0

    for i in range(len(line)):
        count_173 = 0
        count_y = 0

        for j in range(i, len(line)):
            if line[j] == "Y":
                count_y += 1
            
            if j >= i + 2 and line[j - 2:j + 1] == "173":
                count_173 += 1
            
            if count_y > 5:
                break

            if count_y == 5 and count_173 >= 2 and answer < j - i + 1:
                answer = j - i + 1
    
    return answer


line = input()

print(number_9(line))

# 5

from collections import defaultdict


def number_5(line):
    massive = line.split("A")
    massive.pop(0)
    massive = list(filter(None, massive))
    line = "".join(map(lambda x: x[0], massive))

    letter_dict = defaultdict(int)

    for i in line:
        letter_dict[i] += 1
    
    maxi = 0

    for i in letter_dict:
        if maxi < letter_dict[i]:
            maxi = letter_dict[i]
    
    answer = ""

    for i in letter_dict:
        if letter_dict[i] == maxi:
            answer = i
            break
    
    return f"{answer}{maxi}"

print(number_5(input()))