
flowerbed = [0, 0, 1, 0, 0]
n = 1
zeros = 0

flowerbed = [0] + flowerbed + [0]

for i in range(1, len(flowerbed)-1):
    if flowerbed[i]==0:
        if flowerbed[i+1]==0 and flowerbed[i-1]==0:
            zeros += 1
            flowerbed[i] = 1

if zeros >= n:
    print(True)
print(False)