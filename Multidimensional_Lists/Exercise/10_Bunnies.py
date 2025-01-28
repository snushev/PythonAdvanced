def  bunny_spread(matrix):
    for r in range(n):
        for c in range(m):
            if matrix[r][c] == "B":
                for destination in possible_moves:
                    bunny = [r, c]
                    new_move = possible_moves[destination]
                    bunny[0] = r + new_move[0]
                    bunny[1] = c + new_move[1]
                    if bunny[0] < 0:
                        matrix[bunny[0]][bunny[1]] = 'B'
                        matrix[bunny[0]][bunny[1]] = 'B'
                        matrix[bunny[0]][bunny[1]] = 'B'
                    elif bunny[0] >= n:
                        matrix[bunny[0] - 1][bunny[1]] = 'B'
                        matrix[bunny[0]][bunny[1] - 1] = 'B'
                        matrix[bunny[0]][bunny[1] + 1] = 'B'
                    elif bunny[0] < 0:
                        matrix[bunny[0] - 1][bunny[1]] = 'B'
                        matrix[bunny[0] + 1][bunny[1]] = 'B'
                        matrix[bunny[0]][bunny[1] + 1] = 'B'
                    elif bunny[0] >= m:
                        matrix[bunny[0] - 1][bunny[1]] = 'B'
                        matrix[bunny[0] + 1][bunny[1]] = 'B'
                        matrix[bunny[0]][bunny[1] - 1] = 'B'
                    else:
                        matrix[bunny[0] - 1][bunny[1]] = 'B'
                        matrix[bunny[0] + 1][bunny[1]] = 'B'
                        matrix[bunny[0]][bunny[1] - 1] = 'B'
                        matrix[bunny[0]][bunny[1] + 1] = 'B'
    return matrix


n, m = [int(x) for x in input().split()]


player_pos = []
matrix = []
state = ""

for row in range(n):
    matrix.append([])
    for char in input():
        matrix[row].append(char)
    for col in range(m):
        if matrix[row][col] == 'P':
            matrix[row][col].replace( 'P', '.')
            player_pos = [row, col]

possible_moves = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1)
}

move_order = input()

for direction in move_order:
    move = possible_moves[direction]
    row = player_pos[0] + move[0]
    col = player_pos[1] + move[1]

    player_pos = [row, col]

    if row < 0 or row >= n or col < 0 or col >= n:
        state = "won"
        matrix = bunny_spread(matrix)
        break
    if matrix[row][col] == "B":
        state = "lost"
        matrix = bunny_spread(matrix)
        break
    else:
        matrix = bunny_spread(matrix)
        if "P" not in matrix:
            state = "lost"
            break

if state == "won":
    print(f"won: {player_pos[0]} {player_pos[1]}")
else:
    print(f"dead: {player_pos[0]} {player_pos[1]}")

for row in matrix:
    print(*row)