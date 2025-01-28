n = int(input())

matrix = []
ship_pos = [0, 0]
resources = 100

for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == "S":
            matrix[row][col] = "."
            ship_pos = [row, col]

possible_moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while True:
    direction = input()
    move = possible_moves[direction]
    row = ship_pos[0] + move[0]
    col = ship_pos[1] + move[1]
    resources -= 5

    if row < 0 or row >= n or col < 0 or col >= n:
        matrix[ship_pos[0]][ship_pos[1]] = "S"
        print("Mission failed! The spaceship was lost in space.")
        break
    elif matrix[row][col] == "P":
        print(f"Mission accomplished! The spaceship reached Planet B with {resources} resources left.")
        break
    elif matrix[row][col] == "R":
        resources += 10
        if resources > 100:
            resources = 100
    elif matrix[row][col] == "M":
        resources -= 5
        matrix[row][col] = '.'

    if resources == 0:
        print("Mission failed! The spaceship was stranded in space.")
        matrix[row][col] = "S"
        break

    ship_pos = [row, col]

for row in matrix:
    print(*row)

