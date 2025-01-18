rows, cols = input().split(' ')
rows = int(rows)
cols = int(cols)

counter = 0

matrix = [[j for j in input().split()] for i in range(rows)]

for row in range(rows - 1):
    for col in range(cols - 1):
       if matrix[row][col] == matrix[row][col + 1] == matrix[row + 1][col] == matrix[row + 1][col + 1]:
            counter += 1

print(counter)
