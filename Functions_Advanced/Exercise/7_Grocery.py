def grocery_store(**kwargs):

    items = ''
    sorted_grocery = dict(sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0])))

    for item, quantity in sorted_grocery.items():
        items += f"{item}: {quantity}\n"

    return items


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))
print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))
