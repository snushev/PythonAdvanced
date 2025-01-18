n = int(input())

result = []
for _ in range(n):
    result += [int(element) for element in input().split(', ')]

print(result)