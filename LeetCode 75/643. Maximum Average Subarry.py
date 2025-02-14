
nums = [1,12,-5,-6,50,3]
k = 4

curr_sum = max_sum = sum(nums[:k])

for i in range(len(nums)-k+1):
    curr_sum += nums[i+k] - nums[i]
    max_sum = max(curr_sum, max_sum)

print()
