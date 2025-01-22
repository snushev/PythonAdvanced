from functools import reduce

def operate(operator, *args):
    def sum_nums():
        return reduce(lambda x, y: x + y, args)

    def subtract_nums():
        return reduce(lambda x, y: x - y, args)

    def multiply_nums():
        return reduce(lambda x, y: x * y, args)

    def divide_nums():
        return reduce(lambda x, y: x / y, args)

    mapper = {
        '+': sum_nums,
        '-': subtract_nums,
        '*': multiply_nums,
        '/': divide_nums
    }

    function_to_invoke = mapper[operator]
    return function_to_invoke()

print(operate("+", 1, 2, 3))

