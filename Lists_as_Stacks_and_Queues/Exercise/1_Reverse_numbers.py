q = list(map(int, input().split()))
reversed_list = []

while q:
    reversed_list.append(q.pop())

print(*reversed_list, sep=' ')