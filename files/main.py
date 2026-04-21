# from pathlib import Path

# p1 = Path("data/lol.txt")
# p2 = Path("folder") / "data" / "data.txt"
# p3 = Path.home() / "data" / "data.txt"

# print(p1)
# print(p1.exists())
# print(p1.is_file())
# print(p1.is_dir())

# f = open(p1, "r")

# for s in f:
#     print(s)


import hashlib

password = "123445645366454ty54yyu6563245yteru64535gfdhgh"

hash_obj = hashlib.sha512(password.encode("utf-8"))
hex_hash = hash_obj.hexdigest()

print(hex_hash)