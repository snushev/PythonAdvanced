from collections import deque

monsters = deque(int(x) for x in input().split(','))
soldiers = [int(x) for x in input().split(',')]
killed = 0

while monsters and soldiers:
    current_monster = monsters.popleft()
    current_soldier = soldiers.pop()
    diff = abs(current_monster - current_soldier)
    if current_monster <= current_soldier:
        killed += 1
        if diff > 0:
            if len(soldiers) > 0:
                soldiers[-1] += diff
            elif len(soldiers) == 0:
                soldiers.append(diff)
    else:
        if diff > 0:
            monsters.append(diff)

if not monsters:
    print("All monsters have been killed!")
if not soldiers:
    print("The soldier has been defeated.")
print(f"Total monsters killed: {killed}")