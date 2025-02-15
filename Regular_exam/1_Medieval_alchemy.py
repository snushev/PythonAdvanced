from collections import deque

substances = [int(x) for x in input().split(', ')]
crystals = deque([int(x) for x in input().split(', ')])

crafted_potions = []

potions = {
    110: "Brew of Immortality",
    100: "Essence of Resilience",
    90: "Draught of Wisdom",
    80: "Potion of Agility",
    70: "Elixir of Strength"
}

while (substances and crystals) and len(crafted_potions) < 5:
    first_substance = substances.pop()
    first_crystal = crystals.popleft()
    total = first_crystal + first_substance

    if total in potions.keys():
        if potions[total] not in crafted_potions:
            crafted_potions.append(potions[total])
            del(potions[total])
    else:
        for num, pot in potions.items():
            if total >= num and pot not in crafted_potions:
                crafted_potions.append(pot)
                del(potions[num])

                if first_crystal > 20:
                    crystals.append(first_crystal - 20)
                break
        else:
            if first_crystal > 5:
                crystals.append(first_crystal - 5)

if len(crafted_potions) == 5:
    print("Success! The alchemist has forged all potions!")
else:
    print("The alchemist failed to complete his quest.")
if crafted_potions:
    print(f"Crafted potions: {', '.join(crafted_potions)}")

if substances:
    substances = reversed(substances)
    print(f"Substances: {', '.join(map(str, substances))}")
if crystals:
    print(f"Crystals: {', '.join(map(str, crystals))}")