
def merge(nums1, m, nums2, n):
    pnt = -1

    for i in range(len(nums1)):
        if m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[pnt] = nums1[m-1]
                m -= 1
            else:
                nums1[pnt] = nums2[n-1]
                n -=1
            pnt -= 1

    if n > 0:
        for i in range(n):
            nums1[pnt] = nums2[n-1]
            n, pnt = n-1, pnt-1

# nums1 = [1,2,3,0,0,0]
# m = 3
# nums2 = [2,5,6]
# n = 3
nums1 = [2, 0]
m =     1
nums2 = [1]
n = 1
print(merge(nums1, m, nums2, n))
