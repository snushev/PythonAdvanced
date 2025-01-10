nums = tuple([float(element) for element in input().split()])
#nums = tuple(map(float, input().split()))

data = {}
for element in nums:
    data[element] = nums.count(element)

for key, value in data.items():
    print(f"{key:.1f} - {value} times")