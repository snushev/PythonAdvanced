def boom(matrix, i, j, x, y, z, k):
    for r in range(i + x, i + z):
        for c in range(j + y, j + k):
            if matrix[r][c] > 0:
                matrix[r][c] -= current_bomb

    return matrix


n = int(input())

matrix = [[int(j) for j in input().split()] for i in range(n)]

bombs = [x for x in input().split()]

for bomb in bombs:
    i, j = bomb.split(',')
    i = int(i)
    j = int(j)
    current_bomb = matrix[i][j]
    z = 2
    k = 2
    x = -1
    y = -1

    if i == 0:
        x = 0

    if j == 0:
        y = 0

    if i == len(matrix) - 1:
        z = 1

    if j == len(matrix) - 1:
        k = 1

    if current_bomb > 0:
        matrix = boom(matrix, i, j, x, y, z, k)


counter = 0
total_sum = 0
for i in range(len(matrix)):
    for j in matrix[i]:
        if j > 0:
            counter += 1
            total_sum += j

# counter += [[1 for j in matrix[i] if j > 0] for i in range(len(matrix))]

print(f"Alive cells: {counter}")
print(f"Sum: {total_sum}")
for row in matrix:
    print(*row)