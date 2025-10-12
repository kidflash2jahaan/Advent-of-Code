puzzle_input = "iwrupvqb"

import hashlib

i = 1
while True:
    if hashlib.md5((puzzle_input + str(i)).encode()).hexdigest().startswith("00000"):
        break
    i += 1

print(i)