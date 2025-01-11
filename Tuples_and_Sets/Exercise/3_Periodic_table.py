n = int(input())
table = set()

for i in range(n):
    elements = input().split()
    for element in elements:
        table.add(element)

print(*table, sep='\n')
