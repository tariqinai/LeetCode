
candies = [4,2,1,1,2]
extraCandies = 1
my_list = []

for i in range(len(candies)):
    temp = candies[i] + extraCandies
    if  temp >= max(candies[:i] + candies[i:]):
        my_list.append(True)
    else:
        my_list.append(False)

print(my_list)