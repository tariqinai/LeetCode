
def three_sum(nums):
    # i,j,k = 0,1,2
    control = 0
    for idx in range(len(nums)):
        i = idx
        j = idx + 1
        k = j + 1
        while k!=len(nums):
            print(i, j, k)
            k+=1
        control +=1
        if control == 3:
            break
        # j = j + 1
        # k = j + 1


nums_list = [-1,0,1,2,-1,-4]
print(three_sum(nums_list))
