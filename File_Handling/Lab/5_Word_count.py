import re

with open('words.txt') as file:
    searched_words = file.read()

searched_words = searched_words.split()

with open('input.txt') as file:
    text = file.read()

data = {}

for searched_word in searched_words:
    pattern = rf'\b{searched_word}\b'
    result = re.findall(pattern, text, re.IGNORECASE)
    data[searched_word] = len(result)

sorted_data = sorted(data.items(), key=lambda x: -x[1])

with open('output.txt', 'w') as file:
    for word, count in sorted_data:
        file.write(f'{word} - {count}\n')