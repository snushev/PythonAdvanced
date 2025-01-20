data = input().split('|')

matrix = []

for i in range(len(data) - 1, -1 , -1):
    matrix.append([int(x) for x in data[i].strip().split(' ') if x != ''])

flattened = [num for sublist in matrix for num in sublist]
print(*flattened)

# for i in range(len(data) - 1, -1 , -1):
#     row = data[i].split()
#     matrix.append(row)
#
# for row in matrix:
#     print(*row, end=' ')