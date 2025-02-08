def softuni_students(*args, **kwargs):
    sorted_args = sorted(args, key= lambda x: x[1])

    invalid = []
    result = []
    for id_, name in sorted_args:
        if id_ in kwargs:
            result.append(f"*** A student with the username {name} has successfully finished the course {kwargs[id_]}!")
        else:
            invalid.append(name)
    if invalid:
        result.append(f"!!! Invalid course students: {', '.join(invalid)}")
    return '\n'.join(result)

print(softuni_students(
    ('id_1', 'Kaloyan9905'),
    id_1='Python Web Framework',
))
