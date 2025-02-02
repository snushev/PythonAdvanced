def list_roman_emperors(*args, **kwargs):
    successful = {}
    unsuccessful = {}

    for emperor, status in args:
        if status:
            successful[emperor] = 0
        else:
            unsuccessful[emperor] = 0

    for emperor, years in kwargs.items():
        if emperor in successful:
            successful[emperor] = years
        else:
            unsuccessful[emperor] = years

    sorted_successful = dict(sorted(successful.items(), key=lambda x: (-x[1], x[0])))
    sorted_unsuccessful = dict(sorted(unsuccessful.items(), key=lambda x: (x[1], x[0])))

    result = []
    result.append(f"Total number of emperors: {len(args)}")
    if sorted_successful:
        result.append("Successful emperors:")
        for emperor, years in sorted_successful.items():
            result.append(f"****{emperor}: {years}")
    if sorted_unsuccessful:
        result.append("Unsuccessful emperors:")
        for emperor, years in sorted_unsuccessful.items():
            result.append(f"****{emperor}: {years}")

    return '\n'.join(result)

print(list_roman_emperors(("Augustus", True), ("Trajan", True), ("Nero", False),
                          ("Caligula", False), ("Pertinax", False), ("Vespasian", True),
                          Augustus=40, Trajan=19, Nero=14, Caligula=4, Pertinax=4, Vespasian=19,))