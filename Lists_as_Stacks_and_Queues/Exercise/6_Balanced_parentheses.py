sequence = input()

opening_parenthesis = '([{'
closing_parenthesis = ')]}'
stack = []

for char in sequence:
    if char in opening_parenthesis:
        stack.append(char)
    elif char in closing_parenthesis:
        if not stack:
            print('NO')
            break
        last_parenthesis = stack.pop()
        if opening_parenthesis.index(last_parenthesis) != closing_parenthesis.index(char):
            print('NO')
            break

else:
    if stack:
        print('NO')
    else:
        print('YES')