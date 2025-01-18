rows, cols = input().split(', ')
rows = int(rows)
cols = int(cols)

matrix = []

for _ in range(rows):
    row_data = [int(el) for el in input().split(', ')]
    matrix.append(row_data)

max_sum = float("-inf")
sub_matrix = []

for row_index in range(len(matrix) - 1):
    for col_index in range(len(matrix[row_index]) - 1):
        current_el = matrix[row_index][col_index]
        next_to = matrix[row_index][col_index + 1]
        under = matrix[row_index + 1][col_index]
        diagonal = matrix[row_index + 1][col_index + 1]

        current_sum = current_el + next_to + under + diagonal

        if current_sum > max_sum:
            max_sum = current_sum
            sub_matrix = [[current_el, next_to],
                          [under, diagonal]]

print(*sub_matrix[0])
print(*sub_matrix[1])
print(max_sum)