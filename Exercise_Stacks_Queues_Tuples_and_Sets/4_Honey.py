from collections import deque

bees = deque(map(int, input().split(' ')))
nectar = list(map(int, input().split(' ')))
operators = deque(input().split(' '))

total_honey = 0

while bees and nectar:
    current_bee = bees.popleft()
    current_nectar = nectar.pop()
    current_operator = operators.popleft()

    if current_nectar >= current_bee:
        if current_operator == "+":
            total_honey += current_bee + current_nectar
        elif current_operator == "-":
            total_honey += abs(current_bee - current_nectar)
        elif current_operator == "*":
            total_honey += current_bee * current_nectar
        elif current_operator == "/":
            if current_nectar != 0:
                total_honey += current_bee / current_nectar

    else:
        bees.appendleft(current_bee)
        operators.appendleft(current_operator)

print(f"Total honey made: {total_honey}")
if bees:
    print(f"Bees left: {', '.join(map(str, bees))}")
if nectar:
    print(f"Nectar left: {', '.join(map(str, nectar))}")