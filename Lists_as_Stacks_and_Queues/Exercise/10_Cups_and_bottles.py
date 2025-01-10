from collections import deque

cups = deque(map(int, input().split(' ')))
bottles = list(map(int, input().split(' ')))
lost_water = 0

while cups and bottles:
    cup_capacity = cups.popleft()
    bottle_volume = bottles.pop()

    if bottle_volume >= cup_capacity:
        lost_water += bottle_volume - cup_capacity
    else:
        cups.appendleft(cup_capacity - bottle_volume)

if bottles:
    print(f"Bottles: {' '.join(map(str, bottles))}")
elif cups:
    print(f"Cups: {' '.join(map(str, cups))}")

print(f"Wasted litters of water: {lost_water}")