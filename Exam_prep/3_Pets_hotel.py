def accommodate_new_pets(capacity, max_weight, *args):

    accommodated_pets = {}
    result = []
    full = False

    for animal, weight in args:
        if capacity > 0 and weight <= max_weight:
            if animal not in accommodated_pets:
                accommodated_pets[animal] = 0
            accommodated_pets[animal] += 1
            capacity -= 1
        elif capacity == 0:
            result.append(f"You did not manage to accommodate all pets!")
            full = True
            break



    if not full:
        result.append(f"All pets are accommodated! Available capacity: {capacity}.")

    sorted_accommodated = sorted(accommodated_pets)

    result.append("Accommodated pets:")
    for animal in sorted_accommodated:
        result.append(f"{animal}: {accommodated_pets[animal]}")

    return '\n'.join(result)


print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))
print("-------------------")
print(accommodate_new_pets(
    10,
    10.0,
    ("cat", 5.8),
    ("dog", 10.5),
    ("parrot", 0.8),
    ("cat", 3.1),
))
