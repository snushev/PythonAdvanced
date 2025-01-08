from collections import deque

kids = deque(input().split())
n = int(input()) - 1

while len(kids) > 1:
    kids.rotate(-n)
    print(f'Removed {kids.popleft()}')

print(f'Last is {kids[0]}')
