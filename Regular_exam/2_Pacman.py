n = int(input())
matrix = []
player_pos = None
health = 100
stars = 0
freeze = False

for row in range(n):
    matrix.append([x for x in input()])
    for col in range(n):
        if matrix[row][col] == "P":
            matrix[row][col] = "-"
            player_pos = (row, col)
        if matrix[row][col] == "*":
            stars += 1

possible_moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while True:
    direction = input()
    if direction == "end":
        print("Pacman failed to collect all the stars.")
        matrix[player_pos[0]][player_pos[1]] = "P"
        break

    move = possible_moves[direction]
    new_row = (player_pos[0] + move[0]) % n
    new_col = (player_pos[1] + move[1]) % n

    cell = matrix[new_row][new_col]
    if cell == "*":
        stars -= 1
        matrix[new_row][new_col] = '-'
        if stars == 0:
            print(f"Pacman wins! All the stars are collected.")
            matrix[new_row][new_col] = "P"
            break
    elif cell == "G":
        if not freeze:
            health -= 50
            if health <= 0:
                print(f"Game over! Pacman last coordinates [{new_row},{new_col}]")
                matrix[new_row][new_col] = "P"
                break
        else:
            freeze = False
        matrix[new_row][new_col] = '-'
    elif cell == "F":
        freeze = True
        matrix[new_row][new_col] = '-'
    player_pos = (new_row, new_col)

print(f"Health: {health}")
if stars > 0:
    print(f"Uncollected stars: {stars}")
for row in matrix:
    print("".join(row))