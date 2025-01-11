n = int(input())
odd_set = set()
even_set = set()

for i in range(1, n + 1):
    name = input()
    name_points = 0
    ascii_value = 0
    for char in name:
        ascii_value += ord(char)
    name_points += ascii_value // i
    if name_points % 2 == 0:
        even_set.add(name_points)
    else:
        odd_set.add(name_points)

odd_sum = sum(odd_set)
even_sum = sum(even_set)

if odd_sum == even_sum:
    print(", ".join(map(str, odd_set.union(even_set))))
elif odd_sum > even_sum:
    print(", ".join(map(str, odd_set - even_set)))
else:
    print(", ".join(map(str, even_set ^ odd_set)))