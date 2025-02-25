
from collections import defaultdict

# arr = [1,2,2,1,1,3]
arr = [-3,0,1,-3,1,1,1,-3,10,0]
# arr = [1, 2]

my_dict = defaultdict(int)

for val in arr:
    my_dict[val] += 1

if len(set(my_dict.values())) == len(my_dict.keys()):
    print(True)
else:
    print(False)
