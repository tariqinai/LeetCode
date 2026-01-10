
def findMedianSortedArrays(nums1, nums2):
    num3 = (nums1 + nums2)
    num3.sort()
    if len(num3) % 2 != 0:
        return float(num3[len(num3) // 2])
    else:
        return float(
            ((num3[len(num3) // 2]) + (num3[(len(num3) // 2) - 1])) / 2
        )

nums1 = []
nums2 = []
print(findMedianSortedArrays(nums1, nums2))