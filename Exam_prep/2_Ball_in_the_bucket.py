n = 6
matrix = []

points = 0
prize = ''

for row in range(n):
    matrix.append(input().split())

for _ in range(3):
    row, col = input().strip('()').split(', ')
    row, col = int(row), int(col)
    if 0 <= row < n and 0 <= col < n:
        if matrix[row][col] == "B":
            matrix[row][col] = '0'
            for new_row in range(n):
                points += int(matrix[new_row][col])

if points < 100:
    print(f"Sorry! You need {100 - points} points more to win a prize.")
else:
    if 100 <= points <= 199:
        prize = "Football"
    elif 200 <= points <= 299:
        prize = "Teddy Bear"
    else:
        prize = "Lego Construction Set"
    print(f"Good job! You scored {points} points, and you've won {prize}.")