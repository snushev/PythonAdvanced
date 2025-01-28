def plant_garden(available_garden_space: float, *args, **kwargs):
    plant_space_requirements = {plant: space for plant, space in args}
    sorted_requests = dict(sorted(kwargs.items()))
    planted_plants = {}
    all_plants_fully_planted = True

    for plant, requested_quantity in sorted_requests.items():
        if plant in plant_space_requirements:
            space_per_plant = plant_space_requirements[plant]
            max_quantity = int(available_garden_space // space_per_plant)

            if max_quantity >= requested_quantity:
                planted_plants[plant] = requested_quantity
                available_garden_space -= requested_quantity * space_per_plant
            elif max_quantity > 0:
                planted_plants[plant] = max_quantity
                available_garden_space -= max_quantity * space_per_plant
                all_plants_fully_planted = False
            else:
                all_plants_fully_planted = False

    planted_plants_str = "\n".join(f"{plant}: {quantity}" for plant, quantity in sorted(planted_plants.items()))

    if all_plants_fully_planted:
        return f"All plants were planted! Available garden space: {available_garden_space:.1f} sq meters.\nPlanted plants:\n{planted_plants_str}"
    else:
        return f"Not enough space to plant all requested plants!\nPlanted plants:\n{planted_plants_str}"

