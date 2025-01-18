matrix = []

rows, cols = input().split(', ')
rows = int(rows)
cols = int(cols)
total_sum = 0

for i in range(rows):
    numbers = list(map(int, input().split(', ')))
    matrix.append(numbers)

    total_sum += sum(numbers)


print(total_sum)
print(matrix)