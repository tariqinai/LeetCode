
# nums = [1,7,3,6,5,6]
# nums = [1,2,3]
# nums = [-1,-1,-1,-1,-1,0]
nums = [2,1,-1]

leftmost = 0
rightmost = 0
index = 0

for i in range(len(nums)):
    rightmost = sum(nums) - (leftmost + nums[i])
    if rightmost == leftmost:
        index = i
        break
    leftmost += nums[i]

if leftmost == rightmost:
    print(index)
else:
    print(-1)

### Right Code ###

# leftmost = 0
#
# for i in range(len(nums)):
#     rightmost = sum(nums) - (leftmost + nums[i])
#     if rightmost == leftmost:
#         return i
#     leftmost += nums[i]
#
# return -1