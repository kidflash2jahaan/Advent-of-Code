puzzle_input = "uqwqemis"

import hashlib

password = ""
i = 0
while True:
    hash = hashlib.md5((puzzle_input + str(i)).encode()).hexdigest()
    if hash.startswith("00000"):
        password += hash[5]
        print(password)
    if len(password) == 8:
        break
    i += 1