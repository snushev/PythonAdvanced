n = int(input())

sum_ = 0

for i in range(n):
    nums = list(map(int, input().split()))
    sum_ += nums[i]

print(sum_)