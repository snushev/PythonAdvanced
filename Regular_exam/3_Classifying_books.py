def classify_books(*args, **kwargs):
    fiction = {}
    non_fiction = {}
    for category, title in args:
        if category.lower() == "fiction":
            fiction[title] = None
        elif category.lower() == "non_fiction":
            non_fiction[title] = None
    for number, title in kwargs.items():
        if title in fiction.keys():
            fiction[title] = number
        elif title in non_fiction.keys():
            non_fiction[title] = number

    sorted_fiction = sorted(fiction.items(), key=lambda x: x[1])
    sorted_non_fiction = sorted(non_fiction.items(), key=lambda x: x[1], reverse=True)

    result = []

    if fiction:
        result.append("Fiction Books:")
        for title, number in sorted_fiction:
            result.append(f"~~~{number}#{title}")
    if non_fiction:
        result.append("Non-Fiction Books:")
        for title, number in sorted_non_fiction:
            result.append(f"***{number}#{title}")

    return '\n'.join(result)

print(classify_books(
    ("non_fiction", "The Art of War"),
    ("fiction", "The Great Gatsby"),
    ("non_fiction", "A Brief History of Time"),
    ("fiction", "Brave New World"),
    FF1234HH="The Great Gatsby",
    NF3845UU="A Brief History of Time",
    NF3421NN="The Art of War",
    FF1234UU="Brave New World"
))
