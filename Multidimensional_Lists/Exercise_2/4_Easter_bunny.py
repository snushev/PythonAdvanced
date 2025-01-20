def check_max(max_sum_, max_dir, max_steps_):
    if current_sum > max_sum_:
        max_sum_ = current_sum
        max_dir = current_direction
        max_steps_ = steps
    return max_sum_, max_dir, max_steps_

n = int(input())

directions = ["up", "down", "left", "right"]

max_sum = -float('inf')
max_direction = None
max_steps = []
starting_row = 0
starting_col = 0
matrix = []

for i in range(n):
    matrix.append([])
    for index, j in enumerate(input().split()):
        if j == 'B':
            starting_row = i
            starting_col = index
        elif j != "X":
            j = int(j)
        matrix[i].append(j)

for current_direction in directions:
    steps = []
    current_sum = 0

    if current_direction == 'up':
        if starting_row > 0:
            for row in range(starting_row - 1, -1, -1):
                if matrix[row][starting_col] == 'X':
                    break
                elif matrix[row][starting_col] != 'X':
                    steps.append([row, starting_col])
                    current_sum += matrix[row][starting_col]
            max_sum, max_direction, max_steps = check_max(max_sum, max_direction, max_steps)

    elif current_direction == 'down':
        if starting_row < n - 1:
            for row in range(starting_row + 1, n):
                if matrix[row][starting_col] == 'X':
                    break
                elif matrix[row][starting_col] != 'X':
                    steps.append([row, starting_col])
                    current_sum += matrix[row][starting_col]
            max_sum, max_direction, max_steps = check_max(max_sum, max_direction, max_steps)

    elif current_direction == 'left':
        if starting_col > 0:
            for col in range(starting_col - 1, -1, -1):
                if matrix[starting_row][col] == 'X':
                    break
                elif matrix[starting_row][col] != 'X':
                    steps.append([starting_row, col])
                    current_sum += matrix[starting_row][col]
            max_sum, max_direction, max_steps = check_max(max_sum, max_direction, max_steps)

    elif current_direction == 'right':
        if starting_col < n - 1:
            for col in range(starting_col + 1, n):
                if matrix[starting_row][col] == 'X':
                    break
                elif matrix[starting_row][col] != 'X':
                    steps.append([starting_row, col])
                    current_sum += matrix[starting_row][col]
            max_sum, max_direction, max_steps = check_max(max_sum, max_direction, max_steps)

print(max_direction)
for step in max_steps:
    print(step)
print(max_sum)