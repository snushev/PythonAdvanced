n = int(input())
matrix = []
jet_pos = None
armor = 300
enemies = 0

for row in range(n):
    matrix.append([x for x in input()])
    for col in range(n):
        if matrix[row][col] == "J":
            matrix[row][col] = "-"
            jet_pos = (row, col)
        elif matrix[row][col] == "E":
            enemies += 1

possible_moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while True:
    direction = input()

    move = possible_moves[direction]
    new_row = jet_pos[0] + move[0]
    new_col = jet_pos[1] + move[1]

    if 0 <= new_row < n and 0 <= new_col < n:
        if matrix[new_row][new_col] == "E":
            if enemies > 1:
                enemies -= 1
                armor -= 100
                if armor <= 0:
                    matrix[new_row][new_col] = "J"
                    print(f"Mission failed, your jetfighter was shot down! Last coordinates [{new_row}, {new_col}]!")
                    break
                else:
                    matrix[new_row][new_col] = "-"
            elif enemies == 1:
                print("Mission accomplished, you neutralized the aerial threat!")
                matrix[new_row][new_col] = "J"
                break
        elif matrix[new_row][new_col] == "R":
            armor = 300
            matrix[new_row][new_col] = '-'
        jet_pos = (new_row, new_col)

for row in matrix:
    print(''.join(row))
