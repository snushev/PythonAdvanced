def concatenate(*args, **qwargs):
    string = ""
    for element in args:
        string += element
    for key, value in qwargs.items():
        if key in string:
            string = string.replace(key, value)

    return string

print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))