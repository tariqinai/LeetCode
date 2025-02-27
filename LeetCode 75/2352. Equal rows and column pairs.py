
from collections import defaultdict

grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
# grid = [[11,1],[1,11]]
gridC = defaultdict(int)
count = 0

for lst in grid:
    gridC[tuple(lst)] += 1

for i in range(len(grid)):
    temp = tuple(grid[j][i] for j in range(len(grid)))
    if temp in gridC.keys():
        count += gridC[temp]

print(gridC)
print(count)

# 11 1
# 1 11
