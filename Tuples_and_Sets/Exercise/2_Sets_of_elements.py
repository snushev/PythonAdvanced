def filler(tup, set_):
    for i in range(tup):
        num = int(input())
        set_.add(num)
    return set_

t = tuple(map(int, input().split()))
first_set = set()
second_set = set()

filler(t[0], first_set)
filler(t[1], second_set)

intersection = first_set.intersection(second_set)
# intersection = first_set & second_set

print(*intersection, sep='\n')