from collections import deque

chocolates = list(map(int,input().split(',')))
milk_cups = deque(map(int, input().split(',')))

milkshakes = 0

while chocolates and milk_cups and milkshakes < 5:

    chocolate = chocolates.pop()
    milk_cup = milk_cups.popleft()

    if chocolate <= 0 and milk_cup <= 0:
        continue
    if chocolate <= 0:
        milk_cups.appendleft(milk_cup)
        continue
    if milk_cup <= 0:
        chocolates.append(chocolate)
        continue

    if chocolate == milk_cup:
        milkshakes += 1
    else:
        chocolate -= 5
        if chocolate > 0:
            chocolates.append(chocolate)
        milk_cups.append(milk_cup)


if milkshakes == 5:
    print('Great! You made all the chocolate milkshakes needed!')
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join(map(str, chocolates))}")
else:
    print("Chocolate: empty")

if milk_cups:
    print(f"Milk: {', '.join(map(str, milk_cups))}")
else:
    print("Milk: empty")