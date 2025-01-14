# n = int(input())
names = set()

# for _ in range(n):
for _ in range(int(input())):
    # name = input()
    names.add(input())

print(*names, sep='\n')
