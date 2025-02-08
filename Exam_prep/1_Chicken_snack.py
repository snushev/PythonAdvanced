from collections import deque

money = [int(x) for x in input().split()]
price = deque([int(x) for x in input().split()])
bought = 0

while money and price:
    current_money = money.pop()
    current_price = price.popleft()

    if current_price == current_money:
        bought += 1
    elif current_money > current_price:
        change = current_money - current_price
        bought += 1
        if len(money) > 0:
            money[-1] += change
        else:
            money.append(change)

if bought >= 4:
    print(f"Gluttony of the day! Henry ate {bought} foods.")
elif bought == 1:
    print(f"Henry ate: {bought} food.")
elif bought > 1:
    print(f"Henry ate: {bought} foods.")

else:
    print("Henry remained hungry. He will try next weekend again.")