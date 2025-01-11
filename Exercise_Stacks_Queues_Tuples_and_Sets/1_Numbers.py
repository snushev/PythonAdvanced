first_sequence = set(map(int, input().split()))
second_sequence = set(int(x) for x in input().split())

n = int(input())

for _ in range(n):
    command_parts = input().split()
    command = " ".join(command_parts[:2])
    nums = [int(x) for x in command_parts if x.isdigit()]
    if command == "Add First":
        for num in nums:
            first_sequence.add(num)
    elif command == "Add Second":
        for num in nums:
            second_sequence.add(num)
    elif command == "Remove First":
        for num in nums:
            first_sequence.discard(num)
    elif command == "Remove Second":
        for num in nums:
            second_sequence.discard(num)
    elif command == "Check Subset":
        print(first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence))

print(f"{', '.join(map(str, sorted(first_sequence)))}")
print(f"{', '.join(map(str, sorted(second_sequence)))}")