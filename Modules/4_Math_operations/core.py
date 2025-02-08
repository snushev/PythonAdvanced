mapper = {
    "+": lambda a,b: a + b,
    "-": lambda a,b: a - b,
    "*": lambda a,b: a * b,
    "/": lambda a,b: a / b,
    '^': lambda a,b: a ** b,
}

def execute(num1, operator, num2):
    function = mapper[operator]
    return function(num1, num2)