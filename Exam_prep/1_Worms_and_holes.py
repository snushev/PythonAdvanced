from collections import deque

worms = [int(x) for x in input().split()]
holes = deque(int(x) for x in input().split())

initial_worms = len(worms)
matches = 0

while worms and holes:
    current_worm = worms.pop()
    current_hole = holes.popleft()

    if current_worm != current_hole:
        current_worm -= 3
        if current_worm > 0:
            worms.append(current_worm)
    else:
        matches += 1


if matches > 0:
    print(f"Matches: {matches}")
else:
    print("There are no matches.")

if worms:
    print(f"Worms left: {', '.join(map(str, worms))}")
elif matches == initial_worms:
    print("Every worm found a suitable hole!")
else:
    print("Worms left: none")

if holes:
    print(f"Holes left: {', '.join(map(str, holes))}")
else:
    print("Holes left: none")