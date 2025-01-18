n_of_rows = int(input())

matrix = [[int(j) for j in input().split(', ') if int(j) % 2 == 0] for i in range(n_of_rows)]

print(matrix)