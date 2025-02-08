def cookbook(*args):
    sorted_args = sorted(args, key=lambda x: (x[1], x[0]))
    book = {}
    for recipe, cuisine, ingredients in sorted_args:
        if cuisine not in book:
            book[cuisine] = []
        book[cuisine].append({"recipe": recipe, "ingredients": ingredients})

    result = []

    sorted_book = dict(sorted(book.items(), key=lambda x: (-len(x[1]))))
    for cuisine, info in sorted_book.items():
        result.append(f"{cuisine} cuisine contains {len(info)} recipes:")
        for i in range(len(info)):
            result.append(f"  * {info[i]['recipe']} -> Ingredients: {', '.join(info[i]['ingredients'])}")
    return '\n'.join(result)

print(cookbook(
        ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
          ("Chicken Curry", "Indian", ["chicken", "curry paste", "coconut milk", "rice"]),
          ("Caesar Salad", "American", ["romaine lettuce", "croutons", "parmesan", "caesar dressing"]),
          ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
          ("Mushroom Risotto", "Italian", ["arborio rice", "mushrooms", "onion", "parmesan", "broth"]),
          ("Tacos", "Mexican", ["tortillas", "ground beef", "lettuce", "tomato", "cheese"]),
          ("Pad Thai", "Thai", ["rice noodles", "shrimp", "peanuts", "bean sprouts", "tamarind sauce"]),
          ("Chicken Alfredo", "Italian", ["fettuccine", "chicken", "alfredo sauce", "broccoli"])))