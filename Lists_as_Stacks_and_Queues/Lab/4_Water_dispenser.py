from collections import deque

litres = int(input())

people = deque()

name = input()

while name != 'Start':
    people.append(name)
    name = input()

command = input()
while command != 'End':
    if command.startswith('refill'):
        litres += int(command.split()[1])
    else:
        litres_requested = int(command)
        name = people.popleft()
        if litres_requested <= litres:
            litres -= litres_requested
            print(f'{name} got water')
        else:
            print(f'{name} must wait')
    command = input()

print(f"{litres} liters left")