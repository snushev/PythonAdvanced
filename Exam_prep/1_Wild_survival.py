from collections import deque

bees = deque([int(x) for x in input().split()])
bee_eaters = [int(x) for x in input().split()]

while bees and bee_eaters:
    bees_group = bees.popleft()
    eaters_group = bee_eaters.pop()

    while bees_group > 0 and eaters_group > 0:
        if bees_group >= 7:
            bees_group -= 7
            eaters_group -= 1
        else:
            bees_group = 0

    if eaters_group > 0:
        bee_eaters.append(eaters_group)
    elif bees_group > 0:
        bees.append(bees_group)

print("The final battle is over!")
if bees:
    print(f"Bee groups left: {', '.join(map(str, bees))}")
elif bee_eaters:
    print(f"Bee-eater groups left: {', '.join(map(str, bee_eaters))}")
else:
    print("But no one made it out alive!")