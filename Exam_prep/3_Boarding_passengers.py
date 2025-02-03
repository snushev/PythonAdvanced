def boarding_passengers(capacity, *passenger_groups):
    boarding_details = {}
    total_passengers = 0

    for group in passenger_groups:
        num_passengers, benefit_program = group
        if capacity >= num_passengers:
            capacity -= num_passengers
            total_passengers += num_passengers
            if benefit_program in boarding_details:
                boarding_details[benefit_program] += num_passengers
            else:
                boarding_details[benefit_program] = num_passengers

    sorted_details = sorted(boarding_details.items(), key=lambda x: (-x[1], x[0]))

    result = "Boarding details by benefit plan:\n"
    for benefit_program, total in sorted_details:
        result += f"## {benefit_program}: {total} guests\n"

    if total_passengers == sum(group[0] for group in passenger_groups):
        result += "All passengers are successfully boarded!"
    elif capacity == 0:
        result += "Boarding unsuccessful. Cruise ship at full capacity."
    else:
        result += f"Partial boarding completed. Available capacity: {capacity}."

    return result
