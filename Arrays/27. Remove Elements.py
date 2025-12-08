
def removeElement(nums, val):
    j = -1
    for i in range(1, len(nums)):
        if nums[i] != val and nums[j] == val:
            # nums[j], nums[i] = nums[i], nums[j]
            j -= 1
        if nums[i] == val and nums[j] != val:
            nums[j], nums[i] = nums[i], nums[j]
            j -= 1
    print(nums)
    return len(nums)-j

# nums = [3, 2, 2, 3]
# [2, 2, 3, 3]
# val = 3
nums = [0,1,2,2,3,0,4,2]
# [2,2,2,1,3,0,4,0]
val = 2
print(removeElement(nums, val))
