n = int(input())

matrix = [[int(j) for j in input().split(', ')] for i in range(n)]

primary_nums = [matrix[i][i] for i in range(n)]
secondary_nums = [matrix[i][n - 1 - i] for i in range(n)]
primary_diagonal_sum = sum(primary_nums)
secondary_diagonal_sum = sum(secondary_nums)

# for i in range(len(matrix)):
#     primary_diagonal_sum += matrix[i][i]
#     primary_nums.append(matrix[i][i])
#     secondary_diagonal_sum += matrix[i][len(matrix) - 1 - i]
#     secondary_nums.append(matrix[i][len(matrix) - 1 - i])

print(f"Primary diagonal: {', '.join(map(str, primary_nums))}. Sum: {primary_diagonal_sum}")
print(f"Secondary diagonal: {', '.join(map(str, secondary_nums))}. Sum: {secondary_diagonal_sum}")