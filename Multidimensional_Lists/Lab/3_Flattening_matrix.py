n = int(input())

result = []
for _ in range(n):
    result += [int(element) for element in input().split(', ')]

# for _ in range(n):
#     for el in input().split(", "):
#         result.append(int(el))


print(result)
