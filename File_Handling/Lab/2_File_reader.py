total_sum = 0

with open('numbers.txt', 'r') as numbers:
    for line in numbers:
        total_sum += int(line)

print(total_sum)