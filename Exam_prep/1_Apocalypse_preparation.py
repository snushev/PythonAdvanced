from collections import deque

textiles = deque([int(x) for x in input().split()])
medicaments = [int(x) for x in input().split()]

crafted_items = {
    "Patch": 0,
    "Bandage": 0,
    "MedKit": 0
}

healing_items = {
    30: "Patch",
    40: "Bandage",
    100: "MedKit"
}
while textiles and medicaments:
    current_textile = textiles.popleft()
    current_medicament = medicaments.pop()

    total = current_textile + current_medicament

    if total in healing_items.keys():
        crafted_items[healing_items[total]] += 1

    elif total > 100:
        crafted_items["MedKit"] += 1
        medicaments[-1] += total - 100
    else:
        medicaments.append(current_medicament + 10)


if not medicaments and not textiles:
    print("Textiles and medicaments are both empty.")
elif not medicaments:
    print("Medicaments are empty.")
elif not textiles:
    print("Textiles are empty.")

sorted_items = sorted(crafted_items.items(), key=lambda x: (-x[1], x[0]))

for item, count in sorted_items:
    if count > 0:
        print(f"{item} - {count}")

if medicaments:
    print(f"Medicaments left: {', '.join(map(str, reversed(medicaments)))}")
if textiles:
    print(f"Textiles left: {', '.join(map(str, textiles))}")