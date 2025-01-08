from collections import deque

queue = deque()

while True:
    person = input()
    if person == "Paid":
        while queue:
            print(queue.popleft())
    elif person == "End":
        count = len(queue)
        print(f"{count} people remaining.")
        break
    else:
        queue.append(person)

