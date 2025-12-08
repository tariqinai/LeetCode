
def removeDuplicates(nums: list):
    pnt_a = 0
    for i in range(len(nums)-1):
        if nums[i] != nums[i+1]:
            pnt_a += 1
            nums[pnt_a] = nums[i+1]
    return pnt_a+1

#
# def removeDuplicates(nums: list):
#     count = 0
#     var = 0
#     final = []
#     for i in range(len(nums) - 1):
#         if nums[i] == nums[i+1]:
#             count += 1
#         else:
#             final.append(nums[i])
#             var = i
#     final.append(nums[var+1])
#
#     # for i in range(count):
#     #     final.append("_")
#
#     return len(final)
#     # return final
#
nums = [0,0,1,1,1,2,2,3,3,4]
# nums = [1, 1, 2]
print(removeDuplicates(nums))


