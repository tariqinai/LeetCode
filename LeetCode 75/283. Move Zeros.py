
nums = [0, 1, 0, 3, 12]

## Solution 1
# count = nums.count(0)
#
# i=0
# while i < len(nums):
#     if nums[i] == 0:
#         del nums[i]
#     else:
#         i += 1
#
# nums.extend([0]*count)
# print(nums)

## Solution 2

l = 0
for r in range(len(nums)):
    if nums[r]:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
print(nums)