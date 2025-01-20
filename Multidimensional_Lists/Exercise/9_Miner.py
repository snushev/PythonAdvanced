from collections import deque

def find_something(matrix, coals):
    new_cell = matrix[current_row][current_col]
    if new_cell == 'e':
        print(f"Game over! ({current_row}, {current_col})")
        exit()
    elif new_cell == 'c':
        coals -= 1
        matrix[current_row][current_col] = '*'
        if coals == 0:
            print(f"You collected all coal! ({current_row}, {current_col})")
            exit()

    return matrix, coals

n = int(input())
commands = deque(command for command in input().split())

current_row = 0
current_col = 0

# matrix = [[j for j in input().split()] for i in range(n)]
coals = 0

matrix = []
for i in range(n):
    map_row = input().split(' ')
    matrix.append(map_row)
    for j in range(len(map_row)):
        if map_row[j] == 's':
            current_row = i
            current_col = j
        elif map_row[j] == 'c':
            coals += 1

while commands:
    current_command = commands.popleft()
    if current_command == "up" and current_row - 1 >= 0:
        current_row -=1

    elif current_command == "down" and current_row + 1 < n:
        current_row += 1

    elif current_command == "left" and current_col - 1 >= 0:
        current_col -= 1

    elif current_command == "right" and current_col + 1 < n:
        current_col += 1

    matrix, coals = find_something(matrix, coals)


print(f"{coals} pieces of coal left. ({current_row}, {current_col})")
