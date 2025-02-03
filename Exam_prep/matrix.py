n = int(input())
matrix = []
player_pos = None

for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == "P":
            matrix[row][col] = "."
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
        player_pos = (new_row, new_col)


