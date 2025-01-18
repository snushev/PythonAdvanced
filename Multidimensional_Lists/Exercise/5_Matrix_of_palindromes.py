r, c = [int(x) for x in input().split()]

start = ord('a')

for row in range(r):
    for col in range(c):
        print(f"{chr(start + row)}{chr(start + row + col)}{chr(start + row)}", end=' ')
    print()