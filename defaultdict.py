# defaultdict — это подкласс стандартного словаря dict, который автоматически создает значения для отсутствующих ключей.

from collections import defaultdict

dict_1 = {}

# при вызове d['key'] -> ошибка

dict_2 = defaultdict(int)

print(dict_2['key'])

# Создание

dict_3 = defaultdict(int) # будет ставить ноль если ключ отсутсвует

print(dict_3['lol'])

dict_4 = defaultdict(lambda: "нету") # будет ставить "нету" если ключ отсутсвует

print(dict_4['loal'])
