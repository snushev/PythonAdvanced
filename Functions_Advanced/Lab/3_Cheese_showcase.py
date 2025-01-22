def sorting_cheeses(**kwargs):
    sorted_cheese = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))

    result = ""
    for cheese, quantity in sorted_cheese:
        result += cheese + "\n"
        for element in sorted(quantity, reverse=True):
            result += f"{element}\n"
    return result

print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
