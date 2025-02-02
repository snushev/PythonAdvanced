from collections import deque

strength = [int(x) for x in input().split()]
accuracy = deque([int(x) for x in input().split()])

goals_scored = 0

while strength and accuracy:
    current_strength = strength[-1]
    current_accuracy = accuracy[0]
    current_sum = current_strength + current_accuracy
    if current_sum == 100:
        strength.pop()
        accuracy.popleft()
        goals_scored += 1
    elif current_sum < 100:
        if current_strength < current_accuracy:
             strength.pop()
        elif current_strength > current_accuracy:
            accuracy.popleft()
        else:
            accuracy.popleft()
            strength[-1] = current_sum
    elif current_sum > 100:
        current_strength -= 10
        strength[-1] = current_strength
        accuracy.rotate(-1)



if goals_scored == 3:
    print("Paul scored a hat-trick!")
elif goals_scored == 0:
    print("Paul failed to score a single goal.")
elif goals_scored > 3:
    print("Paul performed remarkably well!")
else:
    print("Paul failed to make a hat-trick.")
    
if goals_scored > 0:
    print(f"Goals scored: {goals_scored}")

if strength:
    print(f"Strength values left: {', '.join(map(str, strength))}")
if accuracy:
    print(f"Accuracy values left: {', '.join(map(str, accuracy))}")