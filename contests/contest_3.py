# 1

def number_1(list_1, list_2):
    return [*list_1, *list_2]

inputs = input().split("], ")


if inputs[0][1:] == "":
    inputs[0] = []

else:
    inputs[0] = list(map(int, inputs[0][1:].split(", ")))

if inputs[1][1:-1] == "":
    inputs[1] = []

else:
    inputs[1] = list(map(int, inputs[1][1:-1].split(", ")))

print(number_1(inputs[0], inputs[1]))

# 2

def number_2(list_1):
    return [i * 0.9 for i in list_1 if i > 1000]


inputs = input().split(", ")
inputs[0] = inputs[0][1:]
inputs[-1] = inputs[-1][:-1]

if inputs == [""]:
    print([])

else:
    print(number_2(map(int, inputs)))

# 3

def number_3(dictionary):
    return {value: key for key, value in dictionary.items()}


inputs = eval(input())

print(number_3(inputs))

# 4

def number_4(list_1):
    return [i + 1 for i in range(len(list_1)) if list_1[i][:5] == "Error"]

inputs = eval(input())

print(number_4(inputs))


# 5

def number_5(students, grades):
    return {students[i]: grades[i] for i in range(len(students))}


students, grates = eval(input())

print(number_5(students, grates))

# 6

def number_6(list_1):
    normal_list = []
    answer_list = []

    for i in list_1:
        normal_list += i
    
    for i in normal_list:
        if i not in answer_list:
            answer_list.append(i)
    
    if normal_list == []:
        return "set()"
    
    return "{" + f"{answer_list}"[1:-1] + "}"

inputs = eval(input())

print(number_6(inputs))

# 7

def number_7(matrix):
    return [list(sublist) for sublist in zip(*matrix)]

inputs = eval(input())

print(number_7(inputs))

# 8

def number_8(list_1):
    answer_dict = {}

    for i in list_1:
        if i[0] in answer_dict:
            answer_dict[i[0]].append(i)
        
        else:
            answer_dict[i[0]] = [i]
    
    return answer_dict


inputs = eval(input())

print(number_8(inputs))

# 9

def number_9(interes_1, interes_2, interes_3):
    return sorted(list(set(interes_1) & set(interes_2) & set(interes_3)))


interes_1, interes_2, interes_3 = eval(input())

print(number_9(interes_1, interes_2, interes_3))


# 10

def number_10(list_1, list_2):
    return [(i, j) for i in list_1 for j in list_2]


masti, rangs = eval(input())

print(number_10(masti, rangs))

# 11

def number_11(dict_1, dict_2):
    for i in dict_2:
        if i not in dict_1:
            dict_1[i] = dict_2[i]
        
        else:
            dict_1[i] += dict_2[i]
    
    return dict_1


dict_1, dict_2 = eval(input())

print(number_11(dict_1, dict_2))

# 12


def number_12(list_1):
    answer = []

    for i in list_1:
        if type(i) == type(0):
            answer.append(i)
        else:
            answer += number_12(i)
    
    return answer


inputs = eval(input())

print(number_12(inputs))