rows, cols = [int(x) for x in input().split(', ')]

counter_terrorist = []
matrix = []

for row in range(rows):
    matrix.append(list(input()))
    for col in range(cols):
        if matrix[row][col] == 'C':
            counter_terrorist = [row, col]

possible_moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}
bomb_defused = False
bomb_blown = False
player_on_bomb = False

timer = 16

while timer > 0:
    direction = input()
    if direction == 'defuse':
        if matrix[counter_terrorist[0]][counter_terrorist[1]] != "B":
            timer -= 3

        else:
            player_on_bomb = True
            timer -= 4
            if timer >= 0:
                matrix[counter_terrorist[0]][counter_terrorist[1]] = "D"
                bomb_defused = True
                break
            else:
                matrix[counter_terrorist[0]][counter_terrorist[1]] = "X"
                bomb_blown = True
                break
    else:
        move = possible_moves[direction]
        row = counter_terrorist[0] + move[0]
        col = counter_terrorist[1] + move[1]

        if row < 0 or row >= rows or col < 0 or col >= cols:
            continue
        if matrix[row][col] == 'T':
            matrix[row][col] = '*'
            break

        counter_terrorist = [row, col]
        timer -= 1

if bomb_defused:
    print("Counter-terrorist wins!")
    print(f"Bomb has been defused: {timer} second/s remaining.")
else:
    print("Terrorists win!")
if timer <= 0:
    if not player_on_bomb:
        timer = 0
    print("Bomb was not defused successfully!")
    print(f"Time needed: {abs(timer)} second/s.")
for row in matrix:
    print(*row, sep="")