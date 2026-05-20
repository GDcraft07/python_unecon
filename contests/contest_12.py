# # 1

# import hashlib

# def hash_password(password):
#     return hashlib.sha256(password.encode("utf-8")).hexdigest()

# # 2

# import hashlib

# def verify_password(password, hash):
#     return hashlib.sha256(password.encode("utf-8")).hexdigest() == hash

# # 3

# import hashlib

# def hash_with_salt(password, salt):
#     return hashlib.sha256((password + salt).encode("utf-8")).hexdigest()


# # 4

# import hashlib

# def generate_salt_from_number(n, length=16):
#     return hashlib.sha256(f"{n}".encode('utf-8')).hexdigest()[:length]

# # 5

# import hashlib

# def hash_with_unique_salt(password, user_id):
#     return (hashlib.sha256((password +  hashlib.sha256(f"{user_id}".encode('utf-8')).hexdigest()[:16]).encode("utf-8")).hexdigest()[:16], hashlib.sha256(f"{user_id}".encode('utf-8')).hexdigest()[:16])

# print(hash_with_unique_salt("password", 1)[0][:16])


# # 6

# import hashlib

# def verify_with_salt(password, hash_value, salt):
#     return hashlib.sha256((password + salt).encode("utf-8")).hexdigest() == hash_value

# # 7

# import hashlib


# def add_user(users, username, password, user_id):
#     salt = hashlib.sha256(f"{user_id}".encode("utf-8")).hexdigest()[:16]
#     hash = hashlib.sha256((password + salt).encode("utf-8")).hexdigest()
#     users[username] = {"hash": hash, "salt": salt}

#     return users


# def check_user(users, username, password):
#     try:
#         return users[username]["hash"] == hashlib.sha256((password + users[username]["salt"]).encode("utf-8")).hexdigest()
#     except:
#         return False

# # 8

# import hashlib

# def hash_with_iterations(password, salt, iterations=1000):
#     return hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt.encode("utf-8"), iterations).hex()


# # 9

# import hashlib

# def slow_hash(password, iterations=10000):
#     password = password.encode("utf-8")

#     for _ in range(iterations):
#         password = hashlib.sha256(password).digest()
    
#     return password.hex()


# # 10

# def secure_compare(a, b):
#     if len(a) != len(b):
#         return False
    
#     result = 0

#     for i, j in zip(a, b):
#         result |= ord(i) ^ ord(j)
    
#     return result == 0

# # 11

# import itertools
# import hashlib


# def find_string_by_hash(target_hash, max_length=3):
#     for j in range(1, max_length + 1):    
#         for i in itertools.product("abc", repeat=j):
#             if hashlib.sha256("".join(i).encode("utf-8")).hexdigest() == target_hash:
#                 return "".join(i)
    
#     return None


# 12

import hashlib

def process_auth(commands):
    user_id = 1
    book = {}

    results = []

    for command in commands:
        command = command.split()

        print(commands[0])
        if command[0] == "register":
            if command[1] in book:
                results += ["User already exists"]
            else:
                book[command[1]] = (user_id, hashlib.pbkdf2_hmac("sha256", command[2].encode("utf-8"), f"{user_id}".encode("utf-8"), 1000).hex())
                user_id += 1
                results += ["Registered"]
        
        if command[0] == "login":
            if command[1] in book:
                if hashlib.pbkdf2_hmac("sha256", command[2].encode("utf-8"), f"{book[command[1]][0]}".encode("utf-8"), 1000).hex() == book[command[1]][1]:
                    results += ["Login successful"]
                else:
                    results += ["Wrong username or password"]
            else:
                results += ["Wrong username or password"]
        
    return results


commands = [
    "register alice pass123",
    "register alice pass123",
    "login alice pass123",
    "login alice wrong",
    "login bob pass123"
]
for res in process_auth(commands):
    print(res)