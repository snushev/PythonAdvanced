n, m  = [int(x) for x in input().split(',')]
matrix = []
player_pos = None
cheese = 0
for row in range(n):
    matrix.append([x for x in input()])
    for col in range(m):
        if matrix[row][col] == "M":
            matrix[row][col] = "*"
            player_pos = (row, col)
        if matrix[row][col] == "C":
            cheese += 1

possible_moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while True:
    direction = input()
    if direction == "danger":
        print("Mouse will come back later!")
        matrix[player_pos[0]][player_pos[1]] = "M"
        break

    move = possible_moves[direction]
    new_row = player_pos[0] + move[0]
    new_col = player_pos[1] + move[1]

    if 0 <= new_row < n and 0 <= new_col < m:
        if matrix[new_row][new_col] == "C":
            cheese -= 1
            matrix[new_row][new_col] = '*'
            if cheese == 0:
                matrix[new_row][new_col] = "M"
                print("Happy mouse! All the cheese is eaten, good night!")
                break
        if matrix[new_row][new_col] == "T":
            print("Mouse is trapped!")
            matrix[new_row][new_col] = "M"
            break
        if matrix[new_row][new_col] == "@":
            continue
        player_pos = (new_row, new_col)

    else:
        print("No more cheese for tonight!")
        matrix[player_pos[0]][player_pos[1]] = "M"
        break

for row in matrix:
    print("".join(row))