n = int(input())

matrix = [[int(j) for j in input().split(' ')] for i in range(n)]

primary_nums = [matrix[i][i] for i in range(n)]
secondary_nums = [matrix[i][n - 1 - i] for i in range(n)]
primary_diagonal_sum = sum(primary_nums)
secondary_diagonal_sum = sum(secondary_nums)

print(abs(primary_diagonal_sum - secondary_diagonal_sum))