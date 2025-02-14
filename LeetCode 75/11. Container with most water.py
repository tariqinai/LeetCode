
height = [1,8,6,2,5,4,8,3,7]
start, end = 0, len(height)-1
max_area = 0

while start < end:
    area = abs(start - end) * min(height[start], height[end])
    max_area = max(area, max_area)
    if height[start] < height[end]:
        start += 1
    else:
        end -= 1
