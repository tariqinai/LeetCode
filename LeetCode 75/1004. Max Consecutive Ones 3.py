
nums = [1,1,1,0,0,0,1,1,1,1,0]
# nums = [0, 0, 0, 1, 1]

k = 2
max_ones = 0
start = 0
end = 0

while end < len(nums):
    if nums[end] == 0:
        k -= 1

    while k < 0:
        if nums[start] == 0:
            k += 1
        start += 1

    max_ones = max(max_ones, end-start+1)
    end += 1

print(max_ones)
