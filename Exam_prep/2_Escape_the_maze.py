n = int(input())
matrix = []
player_pos = None
health = 100

for row in range(n):
    matrix.append([x for x in input()])
    for col in range(n):
        if matrix[row][col] == "P":
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
        if matrix[new_row][new_col] == "M":
            health -= 40
            if health <= 0:
                matrix[new_row][new_col] = "P"
                health = 0
                print("Player is dead. Maze over!")
                break
            matrix[new_row][new_col] = "-"
        elif matrix[new_row][new_col] == "H":
            health += 15
            matrix[new_row][new_col] = "-"
            if health > 100:
                health = 100
        elif matrix[new_row][new_col] == "X":
            print("Player escaped the maze. Danger passed!")
            matrix[new_row][new_col] = 'P'
            break

        player_pos = (new_row, new_col)

print(f"Player's health: {health} units")

for row in matrix:
    print("".join(row))
