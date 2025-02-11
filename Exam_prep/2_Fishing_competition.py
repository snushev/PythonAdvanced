QUOTA = 20

n = int(input())
matrix = []
player_pos = None
fish = 0
sank = False

for row in range(n):
    matrix.append([x for x in input()])
    for col in range(n):
        if matrix[row][col] == "S":
            matrix[row][col] = "-"
            player_pos = (row, col)

possible_moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while True:
    direction = input()
    if direction == "collect the nets":
        break
    move = possible_moves[direction]
    new_row = (player_pos[0] + move[0]) % n
    new_col = (player_pos[1] + move[1]) % n

    player_pos = [new_row, new_col]

    if matrix[new_row][new_col].isdigit():
        fish += int(matrix[new_row][new_col])
        matrix[new_row][new_col] = '-'
    elif matrix[new_row][new_col] == 'W':
        fish = 0
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. "
              f"Last coordinates of the ship: [{player_pos[0]},{player_pos[1]}]")
        sank = True
        break

matrix[player_pos[0]][player_pos[1]] = "S"
if not sank:
    if fish >= QUOTA:
        print(f"Success! You managed to reach the quota!")
    else:
        print(f"You didn't catch enough fish and didn't reach the quota! You need {QUOTA - fish} tons of fish more.")
    if fish > 0:
        print(f"Amount of fish caught: {fish} tons.")
    for row in matrix:
        print(''.join(row))