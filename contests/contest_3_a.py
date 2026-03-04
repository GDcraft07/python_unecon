# # 1

# import collections

# def number_1(line):
#     return dict(collections.Counter("".join(line.split(" "))))

# line = input()
# print(number_1(line))

# # 2

# from collections import Counter

# def number_2(line_1, line_2):
#     line_1 = Counter(line_1)
#     line_2 = Counter(line_2)

#     flag = False
#     if len(line_1) == len(line_2):
#         flag = True
#         for i in line_1:
#             if i not in line_2 or line_1[i] != line_2[i]:
#                 flag = False
    
#     return flag

# inputs = input()

# if inputs == "":
#     print(True)

# else:
#     print(number_2(*inputs.split()))

# # 3

# from collections import defaultdict

# def number_3(line):
#     lists = eval(line)
#     print(lists)
#     def_dict = defaultdict(list)
#     for i in lists:
#         def_dict[i[0]] += [i[1]]
    
#     return dict(def_dict)


# line = input()

# print(number_3(line))

# # 4

# from collections import defaultdict

# def number_4(line):
#     lists = eval(line)
#     def_dict = defaultdict(int)

#     for i in lists:
#         def_dict[i] += 1
    
#     return dict(def_dict)


# line = input()

# print(number_4(line))

# # 5

# from collections import Counter

# def number_5(warehouse, sold):
#     warehouse = Counter(eval(warehouse))
#     sold = eval(sold)

#     for i in sold:
#         if i in warehouse:
#             warehouse[i] -= 1

#             if warehouse[i] == 0:
#                 del warehouse[i]
    
#     return dict(warehouse)

# warehouse = input()
# sold = input()

# print(number_5(warehouse, sold))


# # 6

# from collections import Counter

# def number_6(line):
#     lists = eval(line)

#     return Counter(lists).most_common(3)

# line = input()

# print(number_6(line))

# # 7

# from collections import defaultdict

# def numebr_7(line):
#     lists = eval(line)
#     def_dict = defaultdict(set)

#     for i in lists:
#         def_dict[i[0]].add(i[1])
#         def_dict[i[1]].add(i[0])
    
#     for i in def_dict:
#         def_dict[i] = set(sorted(def_dict[i]))
#     return dict(def_dict)


# line = input()

# print(numebr_7(line))


# 8

from collections import Counter

def number_8(line):
    counter = Counter(line)

    for i in range(len(line)):
        if counter[line[i]] == 1:
            return i
    return -1


line = input()

print(number_8(line))