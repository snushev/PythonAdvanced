from string import punctuation

with open('line_numbers.txt') as file:
    lines = file.readlines()

result = ""

for index in range(len(lines)):
    n_chars = 0
    n_punc = 0
    for char in lines[index]:
        if char in punctuation:
            n_punc += 1
        else:
            n_chars += 1
    lines[index] = lines[index].replace('\n', "")
    result += f"Line {index + 1}: {lines[index]} ({n_chars})({n_punc})\n"

with open('line_numbers_output.txt', 'w') as file:
    file.write(result)