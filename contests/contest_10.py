# # 1

# morse_code = {
#     "A": ".-",    "B": "-...",  "C": "-.-.",  "D": "-..", "E": ".",     "F": "..-.",  "G": "--.",   "H": "....",
#     "I": "..",    "J": ".---",  "K": "-.-",   "L": ".-..", "M": "--",    "N": "-.",    "O": "---",   "P": ".--.",
#     "Q": "--.-",  "R": ".-.",   "S": "...",   "T": "-", "U": "..-",   "V": "...-",  "W": ".--",   "X": "-..-",
#     "Y": "-.--",  "Z": "--..", "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....",
#     "6": "-....", "7": "--...", "8": "---..", "9": "----.", " ": ""
# }

# print(" ".join([i for i in map(lambda x: morse_code[x], list(input().upper())) if i != ""]))

# # 2

# users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
#          {'name': 'Helga', 'phone': '555-1618'},
#          {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
#          {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
#          {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
#          {'name': 'John', 'phone': '233-421-32', 'email': ''},
#          {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
#          {'name': 'Alina', 'phone': '+7948-799-2434'},
#          {'name': 'Robert', 'phone': '420-2011', 'email': ''},
#          {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
#          {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
#          {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
#          {'name': 'Roman', 'phone': '+7459-145-8059'},
#          {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
#          {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
#          {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]

# names = []

# for i in users:
#     try:
#         if i["email"] == "":
#             names += [i["name"]]
#     except KeyError:
#         names += [i["name"]]

# print(" ".join(sorted(names)))

# # 3

# from collections import Counter

# count = Counter(input().split())

# print(min([w for w in count if count[w] == max(count.values())]))

# # 4

# number_1 = int(input())
# memory = {}

# for _ in range(number_1):
#     line = input()
#     word, means = line.split(": ")
#     memory[word.lower()] = means

# number_2 = int(input())

# for _ in range(number_2):
#     line = input().lower()
#     try:
#         print(memory[line.lower()])
#     except:
#         print("Не найдено")

# # 5

# from collections import Counter

# print("YES") if Counter(input().lower()) == Counter(input().lower()) else print("NO")

# # 6

# from collections import Counter

# print("YES") if Counter([i.lower() for i in input() if i.isalpha()]) == Counter([i.lower() for i in input() if i.isalpha()]) else print("NO")

# # 7

# number = int(input())
# sinonims = {}

# for _ in range(number):
#     word_1, word_2 = input().split()
#     sinonims[word_1] = word_2
#     sinonims[word_2] = word_1

# word = input()
# print(sinonims[word])

# # 8

# number_1 = int(input())
# city_country = {}

# for _ in range(number_1):
#     line = input().split()
#     country = line[0]
#     city = line[1:]
    
#     for i in city:
#         city_country[i] = country

# number_2 = int(input())

# for _ in range(number_2):
#     city = input()
#     print(city_country[city])

# # 9

# number_1 = int(input())
# book = {}

# for _ in range(number_1):
#     phone, name = input().split()
#     name = name.lower()
    
#     if name not in book:
#         book[name] = []
    
#     book[name] += [phone]

# number_2 = int(input())

# for _ in range(number_2):
#     line = input().lower()
    
#     if line in book:
#         print(" ".join(book[line]))
#     else:
#         print("абонент не найден")

# # 10

# from collections import Counter

# word = input()
# word_count = Counter(word)
# number = int(input())
# memory = {}

# for _ in range(number):
#     line = input()
#     letter, count = line.split(": ")
#     memory[int(count)] = letter

# result = []

# for i in word:
#     result.append(memory[word_count[i]])

# print("".join(result))

answer = "2,4"

start = 2.4
count = 0
while start < 100:
    answer += "x1,3"
    start *= 1.3
    count += 1

print(count)
print(f"{answer}={start:.4f}")