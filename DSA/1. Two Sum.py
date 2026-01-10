
# What we can do is we can create hashmap, iterate through array, search if anything present in hashmap,
# if not move ahead. make sure to use target - value so you know if it present in hashmap. :)

def twoSum(nums, target):
    my_dict = {}
    for idx, x in enumerate(nums):
        if target - x in my_dict:
            return [my_dict[target-x], idx]
        else:
            my_dict[x] = idx
        idx += 1
    # for i, j in nums.enumerate(): Problem is we have to check all numbers not consecutive ones


print(twoSum([2, 7, 11, 15], 9))
