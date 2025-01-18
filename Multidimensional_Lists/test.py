#matrix = []

# 1.
# for row_index in range(3):
#     matrix.append([])
#     for col_index in range(2):
#         matrix[row_index].append(0)

# 1. With comprehension
# matrix = [[0 for j in range(2)] for i in range(3)]

# 2.
# for row_index in range (3):
#     matrix.append([])
#     for element in range(1, 4):
#         matrix[row_index].append(element)

# 2. With comprehension
# matrix = [[j for j in range(1, 4)] for i in range(3)]

#print(matrix)

# 3.
# matrix = [[1, 2, 3], [4, 5, 6]]
# flattened = [num for sublist in matrix for num in sublist]