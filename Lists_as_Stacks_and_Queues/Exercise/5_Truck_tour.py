from collections import deque

number_of_pumps = int(input())
pumps = deque()

for _ in range(number_of_pumps):
    current_fuel, distance = input().split()
    pumps.append([int(current_fuel), int(distance)])

start_position = 0
stops = 0

while stops < number_of_pumps:
    fuel = 0
    for i in range(number_of_pumps):
        fuel += pumps[i][0]
        distance = pumps[i][1]
        if fuel < distance:
            pumps.rotate(-1)
            start_position += 1
            stops = 0
            break
        fuel -= distance
        stops += 1

print(start_position)