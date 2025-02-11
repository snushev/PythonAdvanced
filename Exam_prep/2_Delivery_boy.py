n, m = input().split()
n, m = int(n), int(m)
matrix = []
player_pos = None
start_pos = None
got_pizza = False

for row in range(n):
    matrix.append([x for x in input()]) #(input().split())
    for col in range(m):
        if matrix[row][col] == "B":
            player_pos = (row, col)
            start_pos = (row, col)

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

    if 0 <= new_row < n and 0 <= new_col < m:
        cell = matrix[new_row][new_col]
        if cell == '*':
            continue
        elif cell in '.-':
            matrix[new_row][new_col] = '.'
        elif cell == 'P':
            matrix[new_row][new_col] = 'R'
            got_pizza = True
            print("Pizza is collected. 10 minutes for delivery.")
        elif cell == 'A':
            if got_pizza:
                matrix[new_row][new_col] = 'P'
                print("Pizza is delivered on time! Next order...")
                break
        player_pos = (new_row, new_col)

    else:
        print("The delivery is late. Order is canceled.")
        matrix[start_pos[0]][start_pos[1]] = ' '
        break


for row in matrix:
    print(''.join(row))

