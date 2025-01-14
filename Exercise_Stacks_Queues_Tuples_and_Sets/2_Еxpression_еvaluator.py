import math
from collections import deque

line = input().split()

nums = deque()

operators = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a // b,
}

for char in line:
    if char not in '+-*/':
        nums.append(int(char))
    else:
        while len(nums) > 1:
            first_num = nums.popleft()
            second_num = nums.popleft()
            nums.appendleft(operators[char](first_num, second_num))

# for i in line:
#     first_num = 0
#
#     if i == '+':
#         first_num = nums.popleft()
#         while nums:
#             first_num += nums.popleft()
#         nums.append(int(first_num))
#     elif i == '-':
#         first_num = nums.popleft()
#         while nums:
#             first_num -= nums.popleft()
#         nums.append(int(first_num))
#     elif i == '*':
#         first_num = nums.popleft()
#         while nums:
#             first_num *= nums.popleft()
#         nums.append(int(first_num))
#     elif i == '/':
#         first_num = nums.popleft()
#         while nums:
#             first_num /= nums.popleft()
#         nums.append(math.floor(first_num))
#     else:
#         nums.append(int(i))

print(*nums)