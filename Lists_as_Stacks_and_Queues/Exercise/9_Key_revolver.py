from collections import deque

bullet_price = int(input())
barrel_size = int(input())
bullets = list(map(int, input().split()))
locks = deque(map(int, input().split()))
value = int(input())

total_bullets_used = 0

while bullets or locks:
    if total_bullets_used % barrel_size == 0:
        print("Reloading!")

