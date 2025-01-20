n = int(input())

starting_row = 0
starting_col = 0

matrix = []

for i in range(n):
    row = input().split()
    matrix.append(row)
    for j in range(len(matrix[i])):
        if matrix[i][j] == 'A':
            starting_row = i
            starting_col = j

total_teas = 0

while True:
    direction = input()
    matrix[starting_row][starting_col] = '*'

    if direction == "left":
        if starting_col - 1 >= 0 and matrix[starting_row][starting_col - 1] != "R":
            starting_col -= 1
        else:
            print("Alice didn't make it to the tea party.")
            if starting_col - 1 >= 0:
                matrix[starting_row][starting_col - 1] = '*'
            break

    elif direction == "right":
        if starting_col + 1 < n and matrix[starting_row][starting_col + 1] != "R":
            starting_col += 1
        else:
            print("Alice didn't make it to the tea party.")
            if starting_col + 1 < n:
                matrix[starting_row][starting_col + 1] = '*'
            break

    elif direction == "up":
        if starting_row - 1 >= 0 and matrix[starting_row - 1][starting_col] != "R":
            starting_row -= 1
        else:
            print("Alice didn't make it to the tea party.")
            if starting_row - 1 >= 0:
                matrix[starting_row - 1][starting_col] = '*'
            break

    elif direction == "down":
        if starting_row + 1 < n and matrix[starting_row + 1][starting_col] != "R":
            starting_row += 1
        else:
            print("Alice didn't make it to the tea party.")
            if starting_row + 1 < n:
                matrix[starting_row + 1][starting_col] = '*'
            break

    if matrix[starting_row][starting_col].isdigit():
        total_teas += int(matrix[starting_row][starting_col])

    if total_teas >= 10:
        print("She did it! She went to the party.")
        matrix[starting_row][starting_col] = '*'
        break

for row in matrix:
    print(*row)
