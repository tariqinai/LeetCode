
nums = [1, 1, 1]
# nums = [0,1,1,1,0,1,1,0,1]

start = 0
zero = -1
max_ones = 0

for i in range(len(nums)):
    if nums[i] == 0:
        start = zero + 1
        zero = i
    max_ones = max(max_ones, i - start)

print(max_ones)

# k = 1
# start = 0
# end = 0
# max_num = 0
#
# while end < len(nums):
#     if nums[end] == 0:
#         k -= 1
#
#     while k < 0:
#         if nums[start] == 0:
#             k += 1
#         start += 1
#
#     max_num = max(max_num, end-start)
#     end += 1
#
# print(max_num)