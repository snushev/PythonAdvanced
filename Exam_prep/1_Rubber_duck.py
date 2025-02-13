from collections import deque

time_for_single_task = deque(int(x) for x in input().split())
number_of_tasks = [int(x) for x in input().split()]

total_duckies = {
    "Darth Vader Ducky": 0,
    "Thor Ducky": 0,
    "Big Blue Rubber Ducky": 0,
    "Small Yellow Rubber Ducky": 0
}

while time_for_single_task and number_of_tasks:
    current_time = time_for_single_task.popleft()
    current_tasks = number_of_tasks.pop()

    total = current_tasks * current_time
    if 0 <= total <= 60:
        total_duckies["Darth Vader Ducky"] += 1
    elif 61 <= total <= 120:
        total_duckies["Thor Ducky"] += 1
    elif 121 <= total <= 180:
        total_duckies["Big Blue Rubber Ducky"] += 1
    elif 181 <= total <= 240:
        total_duckies["Small Yellow Rubber Ducky"] += 1
    else:
        number_of_tasks.append(current_tasks - 2)
        time_for_single_task.append(current_time)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
for name, count in total_duckies.items():
    print(f"{name}: {count}")