
def removeElement(nums, val):

    k= 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k

    ############# MY CODE ################
    # j = 0
    # if len(nums) == 1 and nums[0] != val:
    #     return 1
    # elif len(nums) == 1 and nums[0] == val:
    #     return 0
    # elif len(nums) == 0:
    #     return 0
    # else:
    #     for i in range(0, len(nums)):
    #         if nums[j] == val and nums[i] != val:
    #             nums[j], nums[i] = nums[i], nums[j]
    #             j += 1
    #         elif nums[j] != val and nums[i] != val:
    #             j += 1
    #         elif nums[j] == val and nums[i] == val:
    #             pass
    #         elif nums[j] != val and nums[i] == val:
    #             j += 1
    #     return j

nums = [3, 2, 2, 3]
val = 3
# nums = [0,1,2,2,3,0,4,2]
# val = 2
# nums = [3]
# val = 5
# nums = [3, 3]
# val = 5
print(removeElement(nums, val))
