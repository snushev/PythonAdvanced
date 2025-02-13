n, m = [int(x) for x in input().split()]
matrix = []
player_pos = None
moves = 0
opponents_touched = 0

for row in range(n):
    matrix.append(input().split())
    for col in range(m):
        if matrix[row][col] == "B":
            player_pos = (row, col)

possible_moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while True:
    direction = input()
    if direction == "Finish":
        break

    move = possible_moves[direction]
    new_row = player_pos[0] + move[0]
    new_col = player_pos[1] + move[1]

    if 0 <= new_row < n and 0 <= new_col < m:
        cell = matrix[new_row][new_col]
        if cell == 'O':
            continue
        elif cell == 'P':
            opponents_touched += 1
            matrix[new_row][new_col] = "-"
            if opponents_touched == 3:
                moves += 1
                break
        moves += 1
        player_pos = (new_row, new_col)

print("Game over!")
print(f"Touched opponents: {opponents_touched} Moves made: {moves}")