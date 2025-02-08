from core import execute

expression = input().split()

num1 = float(expression[0])
operator = expression[1]
num2 = float(expression[2])

result = execute(num1, operator, num2)
print(f"{result:.2f}")