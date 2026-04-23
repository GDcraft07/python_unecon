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

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml"
}

count = 20

try:
    while True:
        for _ in range(count):
            response = requests.get("https://eatcells.com/", headers=headers)
            print(response.status_code)
        
        print(f"Количество запросов: {count}")
        count *= 2
        time.sleep(1)

except:
    print(f"Вылетело на {count} запросов в секунду")