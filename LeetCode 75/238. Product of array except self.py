
nums = [1, 2, 3, 4]
ans = [1] * len(nums)
suffix = [1] * len(nums)

# Prefix
for i in range(1, len(nums)):
    ans[i] = ans[i-1] * nums[i-1]

for i in range(len(nums)-2, -1, -1):
    suffix[i] = suffix[i+1] * nums[i+1]

for i in range(len(nums)-1):
    ans[i] = ans[i] * suffix[i]

# suffix/ [24, 12, 4, 1]
# prefix/ [1, 1, 2, 6]
# ans/ [24, 12, 8, 6]
