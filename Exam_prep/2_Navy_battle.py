n = int(input())
matrix = []
player_pos = None
mines_hit = 0
cruisers = 0

for row in range(n):
    matrix.append([x for x in input()]) #(input().split())
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

    move = possible_moves[direction]
    new_row = player_pos[0] + move[0]
    new_col = player_pos[1] + move[1]

    if 0 <= new_row < n and 0 <= new_col < n:
        cell = matrix[new_row][new_col]
        if cell == "*":
            mines_hit += 1
            matrix[new_row][new_col] = '-'
            if mines_hit == 3:
                matrix[new_row][new_col] = 'S'
                print(f"Mission failed, U-9 disappeared! Last known coordinates [{new_row}, {new_col}]!")
                break
        elif cell == "C":
            cruisers += 1
            matrix[new_row][new_col] = '-'
            if cruisers == 3:
                print(f"Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
                matrix[new_row][new_col] = 'S'
                break
        player_pos = (new_row, new_col)

for row in matrix:
    print(''.join(row))

