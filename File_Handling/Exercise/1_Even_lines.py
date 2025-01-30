chars_to_replace = ["-", ",", ".", "!", "?"]

with open('even_lines.txt') as file:
    lines = file.readlines()

for index in range(0, len(lines), 2):
    line = lines[index].strip()

    for char_to_replace in chars_to_replace:
        line = line.replace(char_to_replace, '@')

    words = line.split()
    reversed_line = ' '.join(reversed(words))

    print(reversed_line)