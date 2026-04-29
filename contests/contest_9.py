# # 1

# lib = {
#     1: "AEIOULNSTRАВЕИНОРСТ",
#     2: "DGДКЛМПУ",
#     3: "BCMPБГЁЬЯ",
#     4: "FHVWYЙЫ",
#     5: "KЖЗХЦЧ",
#     8: "JXШЭЮ",
#     10: "QZФЩЪ"
# }

# def number_1(line):
#     line = line.upper()

#     sums = 0

#     for i in line:
#         for count, j in lib.items():
#             if i in j:
#                 sums += count
#                 break

#     return sums


# line = input()

# print(number_1(line))

# # 2

# things = {'палатка': 5500, 'спальный мешок': 2250, 'удочка': 1200, 'термос': 1000, 'бутерброды': 820, 'куртка': 600, 'фрукты': 500, 'бинокль': 400, 'рубашка': 300, 'аптечка': 200, 'компас': 100, 'салфетки': 40, 'зажигалка': 20, 'жевачка': 10}

# def number_2(n):
#     answer = {}
#     ves = 0

#     for i in things:
#         if ves + things[i] <= n * 1000:
#             answer[i] = things[i]
#             ves += things[i]

#     return "\n".join(answer.keys())

# n = int(input())

# print(number_2(n))

# # 3

# mails = {
#     'mgu.edu': ['andrei_serov', 'alexander_pushkin', 'elena_belova', 'kirill_stepanov'],
#     'gmail.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],
#     'msu.edu': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],
#     'yandex.ru': ['ekaterina_ivanova', 'glebova_nastya'],
#     'harvard.edu': ['john.doe', 'mark.zuckerberg', 'helen_hunt'],
#     'mail.ru': ['roman.kolosov', 'ilya_gromov', 'masha.yashkina']
# }

# def number_3(mail):
#     answer = []

#     for i in mail:
#         for j in mail[i]:
#             answer += [f"{j}@{i}"]

#     return "\n".join(sorted(answer))

# print(number_3(mails))

# # 4

# number = int(input())
# work_dict = {}

# for i in range(number):
#     line = input().upper().split()
#     work_dict[line[0]] = line[1:]

# number_2 = int(input())

# for i in range(number_2):
#     line = input().upper().replace("EXECUTE", "X").split()
#     if line[0][0] in work_dict[line[1]]:
#         print("OK")
#     else: 
#         print("Access denied")


# # 5
# n = int(input())

# book = {}

# for i in range(n):
#     name, product, count = input().split()

#     if name not in book:
#         book[name] = {}

#     if product not in book[name]:
#         book[name][product] = 0

#     book[name][product] += count

# for name in sorted(book):
#     print(f"{name}:")

#     for product in sorted(book[name]):
#         print(product, book[name][product])

# # 7

# cats = [
#         ('Мартин', 5, 'Алексей', 'Егоров'),
#         ('Фродо', 3, 'Анна', 'Самохина'),
#         ('Вася', 4, 'Андрей', 'Белов'),
#         ('Муся', 7, 'Игорь', 'Бероев'),
#         ('Изольда', 2, 'Игорь', 'Бероев'),
#         ('Снейп', 1, 'Марина', 'Апраксина'),
#         ('Лютик', 4, 'Виталий', 'Соломин'),
#         ('Снежок', 3, 'Марина', 'Апраксина'),
#         ('Марта', 5, 'Сергей', 'Колесников'),
#         ('Буся', 12, 'Алена', 'Федорова'),
#         ('Джонни', 10, 'Игорь', 'Андропов'),
#         ('Мурзик', 1, 'Даниил', 'Невзоров'),
#         ('Барсик', 2, 'Виталий', 'Соломин'),
#         ('Рыжик', 7, 'Владимир', 'Медведев'),
#         ('Матильда', 8, 'Андрей', 'Белов'),
#         ('Гарфилд', 3, 'Александр', 'Березуев')
#     ]

# big_bosss = {}

# for i in cats:
#     cat, age, name, lastname = i
#     big_boss = name + " " + lastname

#     if big_boss not in big_bosss:
#         big_bosss[big_boss] = []

#     big_bosss[big_boss].append(f"{cat}, {age}")

# for i in big_bosss:
#     print(f"{i}: {'; '.join(big_bosss[i])}")


# 6

# from collections import defaultdict


# dict1 = {'яблоки': 100, 'бананы': 333, 'груши': 200,
#          'апельсины': 300, 'ананасы': 45, 'лимоны': 98,
#      	'сливы': 76, 'манго': 34, 'виноград': 90, 'лаймы': 230}
# dict2 = {'яблоки': 300, 'груши': 200, 'бананы': 400,
#      	'малина': 777, 'ананасы': 12, 'лаймы': 123, 'черника': 111, 'арбузы': 666}

# result = defaultdict(int)

# for key, value in dict1.items():
#     result[key] += value

# for key, value in dict2.items():
#     result[key] += value

# result = dict(sorted(result.items()))

# print(result)


# # 8

# from collections import Counter

# line = input().lower()

# for i in ",.!?":
#     line = line.replace(i, "")

# line = line.split()

# count = Counter(line)

# answer_count = min(count.values())

# answer = [i for i in count if count[i] == answer_count]

# print(min(answer))

# # 9

# from collections import defaultdict

# line = input().split()

# dictt = defaultdict(int)
# answer = []

# for i in line:
#     dictt[i] += 1
#     value = dictt[i] - 1
#     answer += [f"{i}_{value}" if value else f"{i}"]


# print(" ".join(answer))