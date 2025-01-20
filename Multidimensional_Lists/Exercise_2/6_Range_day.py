SIZE = 5

matrix = []
alice = []
targets = 0

for row in range(SIZE):
    matrix.append(input().split())
    for col in range(SIZE):
        if matrix[row][col] == 'A':
            alice = [row, col]
        elif matrix[row][col] == 'x':
            targets += 1

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

targets_down = []
original_targets = targets

for _ in range(int(input())):
    command = input().split()
    if command[0] == 'shoot':
        row = alice[0] + directions[command[1]][0]
        col = alice[1] + directions[command[1]][1]

        while 0 <= row < SIZE and 0 <= col < SIZE:
            if matrix[row][col] == 'x':
                matrix[row][col] = '.'
                targets -= 1
                targets_down.append([row, col])
                break
            row += directions[command[1]][0]
            col += directions[command[1]][1]

        if targets == 0:
            print(f"Training completed! All {original_targets} targets hit.")
            break

    elif command[0] == 'move':
        steps = int(command[2])
        row = alice[0] + directions[command[1]][0] * steps
        col = alice[1] + directions[command[1]][1] * steps

        if 0 <= row < SIZE and 0 <= col < SIZE and matrix[row][col] == '.':
            matrix[alice[0]][alice[1]] = '.'
            alice = [row, col]
            matrix[alice[0]][alice[1]] = 'A'

if targets > 0:
    print(f"Training not completed! {targets} targets left.")

[print(coord) for coord in targets_down]
