puzzle_input = "R4, R4, L1, R3, L5, R2, R5, R1, L4, R3, L5, R2, L3, L4, L3, R1, R5, R1, L3, L1, R3, L1, R2, R2, L2, R5, L3, L4, R4, R4, R2, L4, L1, R5, L1, L4, R4, L1, R1, L2, R5, L2, L3, R2, R1, L194, R2, L4, R49, R1, R3, L5, L4, L1, R4, R2, R1, L5, R3, L5, L4, R4, R4, L2, L3, R78, L5, R4, R191, R4, R3, R1, L2, R1, R3, L1, R3, R4, R2, L2, R1, R4, L5, R2, L2, L4, L2, R1, R2, L3, R5, R2, L3, L3, R3, L1, L1, R5, L4, L4, L2, R5, R1, R4, L3, L5, L4, R5, L4, R5, R4, L3, L2, L5, R4, R3, L3, R1, L5, R5, R1, L3, R2, L5, R5, L3, R1, R4, L5, R4, R2, R3, L4, L5, R3, R4, L5, L5, R4, L4, L4, R1, R5, R3, L1, L4, L3, L4, R1, L5, L1, R2, R2, R4, R4, L5, R4, R1, L1, L1, L3, L5, L2, R4, L3, L5, L4, L1, R3"

x = 0
y = 0
compass = 0
first_x = 0.1
first_y = 0.1
previous_x_list = [0]
previous_y_list = [0]

for instruction in puzzle_input.split(", "):
    direction = instruction[0]
    distance = int(instruction[1:])

    if direction == "R":
        compass += 1
    else:
        compass -= 1
    if compass > 3:
        compass = 0
    if compass < 0:
        compass = 3

    for i in range(distance):
        match compass:
            case 0:
                y += 1
            case 1:
                x += 1
            case 2:
                y -= 1
            case 3:
                x -= 1
        

        for j in range(len(previous_x_list)):
            if previous_x_list[j] == x and previous_y_list[j] == y and first_x == 0.1 and first_y == 0.1:
                first_x = x
                first_y = y
        
        previous_x_list.append(x)
        previous_y_list.append(y)
        

print(abs(first_x)+abs(first_y))
