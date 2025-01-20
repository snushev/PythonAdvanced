n = int(input())

matrix = [[int(j) for j in input().split()]for i in range(n)]

while True:
    command = input()
    if command == "END":
        break

    command = command.split()
    action = command[0]
    row_index = int(command[1])
    col_index = int(command[2])
    value = int(command[3])
    if row_index >= n or row_index < 0 or col_index < 0 or col_index >= n:
        print("Invalid coordinates")
        continue

    if action == "Add":
        matrix[row_index][col_index] += value
    elif action == "Subtract":
        matrix[row_index][col_index] -= value

for row in matrix:
    print(*row)