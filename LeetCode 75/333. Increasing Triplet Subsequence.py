
nums = [5, 10, 6, 7, 11]
n1 = n2 = float('inf')

for num in nums:
    if num <= n1:
        n1 = num
    elif num <= n2:
        n2 = num
    else:
        print(True)