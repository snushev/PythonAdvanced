def func_executor(*args):

    res = ""
    for func, value in args:
        result = func(*value)
        res += f"{func.__name__} - {result}\n"
    return res


def make_upper(*strings):
    result = tuple(s.upper() for s in strings)
    return result

def make_lower(*strings):
    result = tuple(s.lower() for s in strings)
    return result

print(func_executor(
    (make_upper, ("Python", "softUni")),
    (make_lower, ("PyThOn",)),))