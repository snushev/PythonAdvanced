n = int(input())
matrix = []
player_pos = None
money = 100

for row in range(n):
    matrix.append([x for x in input()])
    for col in range(n):
        if matrix[row][col] == "G":
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
    if direction == 'end':
        matrix[player_pos[0]][player_pos[1]] = 'G'
        print(f"End of the game. Total amount: {money}$")
        break

    move = possible_moves[direction]
    new_row = player_pos[0] + move[0]
    new_col = player_pos[1] + move[1]

    if 0 <= new_row < n and 0 <= new_col < n:
        if  matrix[new_row][new_col] == "W":
            money += 100
            matrix[new_row][new_col] = "-"

        elif  matrix[new_row][new_col] == "P":
            money -= 200
            matrix[new_row][new_col] = "-"
            if money <= 0:
                print("Game over! You lost everything!")
                break
        elif matrix[new_row][new_col] == 'J':
            money += 100000
            matrix[new_row][new_col] = 'G'
            print(f"You win the Jackpot!\n"
                  f"End of the game. Total amount: {money}$")
            break
        player_pos = (new_row, new_col)
    else:
        matrix[new_row][new_col] = "-"
        print("Game over! You lost everything!")
        break


if money > 0:
    for row in matrix:
        print("".join(row))