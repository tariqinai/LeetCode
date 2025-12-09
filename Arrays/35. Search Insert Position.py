
def searchInsert(nums, target):
    # i = 0
    for i in range(len(nums)):
        if nums[i] == target:
            return i
        elif nums[i] > target:
            return i
    # return i+1
    return len(nums)


# nums = [1,3,5,6]
# target = 5
nums = [1,3,5,6]
target = 7
print(searchInsert(nums, target))