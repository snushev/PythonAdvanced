row_count, col_count = input().split(', ')
row_count = int(row_count)
col_count = int(col_count)

matrix = [[int(el) for el in input().split()] for row in range(row_count)]

for col_index in range(col_count):
    col_sum = 0
    for row_index in range(row_count):
        col_sum += matrix[row_index][col_index]
    print(col_sum)