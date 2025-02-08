def draw_cards(*args, **kwargs):
    monsters = set()
    spells = set()

    for name, type_ in args:
        if type_ == "monster":
            monsters.add(name)
        elif type_ == "spell":
            spells.add(name)

    for name, type_ in kwargs.items():
        if type_ == "monster":
            monsters.add(name)
        elif type_ == "spell":
            spells.add(name)

    result = []
    sorted_monsters = sorted(monsters, reverse=True)
    sorted_spells = sorted(spells)

    if sorted_monsters:
        result.append("Monster cards:")
        for card in sorted_monsters:
            result.append(f"  ***{card}")
    if sorted_spells:
        result.append("Spell cards:")
        for card in sorted_spells:
            result.append(f"  $$${card}")

    return '\n'.join(result)

print(draw_cards(("celtic guardian", "monster"), ("earthquake", "spell"), ("fireball", "spell"),
                 raigeki="spell", destroy="spell",))