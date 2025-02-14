
nums = [1, 2, 3, 4]
nums = [4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4]
k = 2
count = 0
nums.sort()
print(nums)

start, end = 0, len(nums)-1
while start < end:
    print(start, end, nums[start] + nums[end])
    if nums[start] + nums[end] == k:
        count += 1
        start += 1
        end -= 1
    elif nums[start] + nums[end] > k:
        end -= 1
    elif nums[start] + nums[end] < k:
        start += 1

print(count)
