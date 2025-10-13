puzzle_input = "1113222113"


previous_result = puzzle_input
i = 0
while i < 40:
    number_groups = ['remove']
    for char in previous_result:
        if number_groups[-1].endswith(char):
            number_groups[-1] += char
        else:
            number_groups.append(char)

    number_groups.remove('remove')

    result = ""
    for number_group in number_groups:
        result += str(len(number_group))
        result += number_group[0]

    previous_result = result
    i += 1

print(len(previous_result))