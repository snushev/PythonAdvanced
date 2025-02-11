from collections import deque

materials = [int(x) for x in input().split()]
magic_level = deque([int(x) for x in input().split()])

gifts_made = {"Gemstone": 0,
               "Porcelain Sculpture": 0,
               "Gold": 0,
               "Diamond Jewellery": 0,
               }

while materials and magic_level:
    current_material = materials.pop()
    current_magic = magic_level.popleft()
    current_sum = current_material + current_magic

    if current_sum < 100:
        if current_sum % 2 == 0:
            current_material *= 2
            current_magic *= 3
            current_sum = current_material + current_magic
        elif current_sum % 2 != 0:
            current_sum *= 2
    if current_sum > 499:
        current_sum //= 2
        if current_sum > 499:
            continue

    if 100 <= current_sum <= 199:
        gifts_made["Gemstone"] += 1
    elif 200 <= current_sum <= 299:
        gifts_made["Porcelain Sculpture"] += 1
    elif 300 <= current_sum <= 399:
        gifts_made["Gold"] += 1
    elif 400 <= current_sum <= 499:
        gifts_made["Diamond Jewellery"] += 1

if (gifts_made["Gemstone"] > 0 and gifts_made["Porcelain Sculpture"] > 0) or (gifts_made["Gold"] > 0 and gifts_made["Diamond Jewellery"] > 0):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(map(str, materials))}")
if magic_level:
    print(f"Magic left: {', '.join(map(str, magic_level))}")

sorted_gifts = sorted(gifts_made.items(), key=lambda x: x[0])

for gift, count in sorted_gifts:
    if count > 0:
        print(f"{gift}: {count}")
