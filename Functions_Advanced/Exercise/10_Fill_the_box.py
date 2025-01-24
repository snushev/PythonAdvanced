def fill_the_box(*args):
    height = args[0]
    length = args[1]
    width = args[2]

    size = height * length * width
    for i in range(3, len(args) - 1):
        if isinstance(args[i], int):
            size -= args[i]

    if size > 0:
        return f"There is free space in the box. You could put {size} more cubes."
    else:
        return f"No more free space! You have {abs(size)} more cubes."

print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))