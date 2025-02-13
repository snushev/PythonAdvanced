n = int(input())
moves = [x for x in input().split(', ')]
matrix = []
player_pos = None
hazelnuts = 0
for row in range(n):
    matrix.append([x for x in input()])
    for col in range(n):
        if matrix[row][col] == "s":
            player_pos = (row, col)

possible_moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for current_move in moves:

    move = possible_moves[current_move]
    new_row = player_pos[0] + move[0]
    new_col = player_pos[1] + move[1]

    if 0 <= new_row < n and 0 <= new_col < n:
        if matrix[new_row][new_col] == "h":
            hazelnuts += 1
            matrix[new_row][new_col] = '*'
            if hazelnuts == 3:
                print("Good job! You have collected all hazelnuts!")
                print(f"Hazelnuts collected: {hazelnuts}")

                exit()
        elif matrix[new_row][new_col] == "t":
            print("Unfortunately, the squirrel stepped on a trap...")
            print(f"Hazelnuts collected: {hazelnuts}")
            exit()
        player_pos = (new_row, new_col)
    else:
        print("The squirrel is out of the field.")
        print(f"Hazelnuts collected: {hazelnuts}")
        exit()

print("There are more hazelnuts to collect.")
print(f"Hazelnuts collected: {hazelnuts}")
