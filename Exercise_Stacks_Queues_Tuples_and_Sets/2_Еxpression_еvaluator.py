import math
from collections import deque

line = input().split()

nums = deque()

for i in line:
    first_num = 0

    if i == '+':
        first_num = nums.popleft()
        while nums:
            first_num += nums.popleft()
        nums.append(int(first_num))
    elif i == '-':
        first_num = nums.popleft()
        while nums:
            first_num -= nums.popleft()
        nums.append(int(first_num))
    elif i == '*':
        first_num = nums.popleft()
        while nums:
            first_num *= nums.popleft()
        nums.append(int(first_num))
    elif i == '/':
        first_num = nums.popleft()
        while nums:
            first_num /= nums.popleft()
        nums.append(math.floor(first_num))
    else:
        nums.append(int(i))

print(*nums)