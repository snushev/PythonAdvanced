from collections import deque

boxes_with_materials = list(map(int, input().split()))
magic_values = deque(map(int, input().split()))

crafted_items = {}

presents = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}

while boxes_with_materials and magic_values:
    first_box = boxes_with_materials.pop()
    first_magic = magic_values.popleft()
    if first_box == 0 or first_magic == 0:
        if first_box == 0 and first_magic == 0:
            pass
        elif first_magic == 0:
            boxes_with_materials.append(first_box)
        elif first_box == 0:
            magic_values.appendleft(first_magic)
    magic_level = first_box * first_magic

    if magic_level in presents.keys():
        if presents[magic_level] not in crafted_items:
            crafted_items[presents[magic_level]] = 0
        crafted_items[presents[magic_level]] += 1
    elif magic_level < 0:
        new_sum = first_box + first_magic
        boxes_with_materials.append(new_sum)
    elif magic_level not in presents.keys() and magic_level > 0:
        first_box += 15
        boxes_with_materials.append(first_box)

if ("Doll" in crafted_items and "Wooden train" in crafted_items) or ("Teddy bear" in crafted_items and "Bicycle" in crafted_items):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if boxes_with_materials:
    print(f"Materials left: {', '.join(map(str, reversed(boxes_with_materials)))}")
if magic_values:
    print(f"Magic left: {', '.join(map(str, magic_values))}")

for item, count in sorted(crafted_items.items()):
    print(f"{item}: {count}")