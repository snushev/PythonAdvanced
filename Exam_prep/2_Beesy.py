n = int(input())
matrix = []
player_pos = None
energy = 15
nectar = 0
bee_on_hive = False
refill = True

for row in range(n):
    matrix.append([x for x in input()])
    for col in range(n):
        if matrix[row][col] == "B":
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

    new_row = (player_pos[0] + move[0]) % n
    new_col = (player_pos[1] + move[1]) % n

    energy -= 1

    if matrix[new_row][new_col].isdigit():
        nectar += int(matrix[new_row][new_col])
        matrix[new_row][new_col] = '-'
    elif matrix[new_row][new_col] == "H":
        matrix[new_row][new_col] = 'B'
        bee_on_hive = True
        break

    player_pos = (new_row, new_col)


    if energy == 0:
        if nectar > 30 and refill:
            energy = nectar - 30
            nectar = 30
            refill = False
        else:
            matrix[new_row][new_col] = 'B'
            break

if bee_on_hive and nectar >= 30:
    print(f"Great job, Beesy! The hive is full. Energy left: {energy}")
elif bee_on_hive and nectar < 30:
    print(f"Beesy did not manage to collect enough nectar.")
elif energy == 0 and not bee_on_hive:
    print("This is the end! Beesy ran out of energy.")

for row in matrix:
    print(*row, sep="")