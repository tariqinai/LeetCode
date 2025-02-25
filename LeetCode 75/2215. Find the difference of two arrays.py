
nums1 = [1, 2, 3]
nums2 = [2, 4, 6]

nums1Set = set(nums1)
nums2Set = set(nums2)

res1, res2 = set(), set()
for num in nums1Set:
    if num not in nums2Set:
        res1.add(num)

for num in nums2Set:
    if num not in nums1Set:
        res2.add(num)

print([list(res1), list(res2)])
