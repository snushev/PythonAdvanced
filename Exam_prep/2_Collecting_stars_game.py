n = int(input())

matrix = []
player_pos = [0, 0]
stars = 2

for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == "P":
            matrix[row][col] = "."
            player_pos = [row, col]

possible_moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while 0 < stars < 10:
    direction = input()
    move = possible_moves[direction]
    row = player_pos[0] + move[0]
    col = player_pos[1] + move[1]

    if row < 0 or row >= n or col < 0 or col >= n:
        player_pos = [0, 0]
        if matrix[0][0] == "*":
            stars += 1
            matrix[0][0] = "."
    elif matrix[row][col] == "*":
        stars += 1
        matrix[row][col] = "."
        player_pos = [row, col]
    elif matrix[row][col] == "#":
        stars -= 1
    else:
        player_pos = [row, col]



if stars == 10:
    print("You won! You have collected 10 stars.")
else:
    print("Game over! You are out of any stars.")

print(f"Your final position is {player_pos}")

matrix[player_pos[0]][player_pos[1]] = "P"

for row in matrix:
    print(*row)