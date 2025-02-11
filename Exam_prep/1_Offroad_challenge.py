from collections import deque

fuel_sequence = [int(x) for x in input().split()]
consumption_index = deque([int(x) for x in input().split()])
fuel_needed = deque([int(x) for x in input().split()])
altitude_counter = 0
reached_altitudes = []
all_altitudes = True

while fuel_sequence and consumption_index:
    current_fuel = fuel_sequence.pop()
    current_index = consumption_index.popleft()
    current_needed = fuel_needed.popleft()

    result = current_fuel - current_index
    altitude_counter += 1
    if result >= current_needed:
        print(f"John has reached: Altitude {altitude_counter}")
        reached_altitudes.append(f"Altitude {altitude_counter}")
    else:
        print(f"John did not reach: Altitude {altitude_counter}")
        print("John failed to reach the top.")
        all_altitudes = False
        break

if reached_altitudes and not all_altitudes:
    print(f"Reached altitudes: {', '.join(reached_altitudes)}")
elif not reached_altitudes:
    print("John didn't reach any altitude.")
if all_altitudes:
    print("John has reached all the altitudes and managed to reach the top!")