import requests
import time

# глянуть что такое протакол RAST, сделать базу данных по клиентам с https://jsonplaceholder.typicode.com/users


response = requests.get("https://jsonplaceholder.typicode.com/users/1")

# print(response.status_code)
# print(response.headers)
# print(response.text)
# print(response.content)
# print(response.url)
# print(response.json())
# print(response.encoding)
# print(response.cookies)
# print(response.elapsed)
# print(response.request)
# print(response.ok)
# print(response.raise_for_status())
