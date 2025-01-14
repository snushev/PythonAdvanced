from collections import deque

initial_colors = deque(input().split())

primary_colors = {"red", "yellow", "blue"}
secondary_colors = {"orange", "purple", "green"}
color_requirements = {
    "orange": {"red", "yellow"},
    "purple": {"red", "blue"},
    "green": {"yellow", "blue"},
}

found_colors = []

while initial_colors:
    if len(initial_colors) == 1:
        first_part = initial_colors.pop()
        second_part = ""
    else:
        first_part = initial_colors.popleft()
        second_part = initial_colors.pop()

    combined_color = first_part + second_part
    reversed_color = second_part + first_part

    if combined_color in primary_colors or combined_color in secondary_colors:
        found_colors.append(combined_color)
    elif reversed_color in primary_colors or reversed_color in secondary_colors:
        found_colors.append(reversed_color)
    else:
        first_part = first_part[:-1]
        second_part = second_part[:-1]
        midpoint = len(initial_colors) // 2
        if len(initial_colors) % 2 != 0:
            midpoint += 1
        if second_part:
            initial_colors.insert(midpoint, second_part)
        if first_part:
            initial_colors.insert(midpoint, first_part)

final_colors = []
for color in found_colors:
    if color in primary_colors:
        final_colors.append(color)
    elif color in secondary_colors:
        required_colors = color_requirements[color]
        if required_colors.issubset(set(found_colors)):
            final_colors.append(color)

print(final_colors)
