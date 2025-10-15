puzzle_input = 29000000

presents = []
house = 0
while True:
    house += 1
    presents.append(0)

    elf = 0
    while elf < house:
        elf += 1
        if house % elf == 0:
            presents[-1] += elf * 10

    if presents[-1] >= puzzle_input:
        break

    print(house)

print(presents)