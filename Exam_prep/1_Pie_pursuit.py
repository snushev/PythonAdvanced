from collections import deque

contestants = deque([int(x) for x in input().split()])
pies = [int(x) for x in input().split()]

while contestants and pies:
    current_contestant = contestants.popleft()
    current_pie = pies.pop()
    if current_contestant >= current_pie:
        current_contestant -= current_pie
        if current_contestant > 0:
            contestants.append(current_contestant)
    elif current_pie > current_contestant:
        current_pie -= current_contestant
        if current_pie > 1:
            pies.append(current_pie)
        elif len(pies) > 0:
            pies[-1] += 1
        elif current_pie == 1 and len(pies) == 0:
            pies.append(current_pie)

if not pies and contestants:
    print("We will have to wait for more pies to be baked!" )
    print(f"Contestants left: {', '.join(map(str, contestants))}")
elif not pies and not contestants:
    print("We have a champion!")
if not contestants and pies:
    print("Our contestants need to rest!")
    print(f"Pies left: {', '.join(map(str, pies))}")