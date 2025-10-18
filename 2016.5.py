puzzle_input = "uqwqemis"

import hashlib

password_list = ["_", "_", "_", "_", "_", "_", "_", "_"]
i = 0
while True:
    hash = hashlib.md5((puzzle_input + str(i)).encode()).hexdigest()
    if hash.startswith("00000"):
        try:
            if password_list[int(hash[5])] == "_":
                password_list[int(hash[5])] = hash[6]
                print("".join(password_list))
        except:
            pass
    if "_" not in password_list:
        break
    i += 1