from collections import deque

bullet_price = int(input())
barrel_size = int(input())
bullets = list(map(int, input().split()))
locks = deque(map(int, input().split()))
value = int(input())

total_bullets_used = 0

while bullets and locks:
    current_bullet = bullets.pop()
    current_lock = locks.popleft()
    total_bullets_used += 1
    if current_bullet <= current_lock:
        print('Bang!')
    else:
        print('Ping!')
        locks.appendleft(current_lock)
    if total_bullets_used % barrel_size == 0 and bullets:
        print("Reloading!")


if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    money_won = value - (bullet_price * total_bullets_used)
    print(f"{len(bullets)} bullets left. Earned ${int(money_won)}")