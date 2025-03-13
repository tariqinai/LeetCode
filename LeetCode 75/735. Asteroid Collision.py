
# asteroids = [5,10,-5]
# asteroids = [8,-8]
asteroids = [10,2,-5]
stack = []

for asteroid in asteroids:
    while stack and asteroid < 0 < stack[-1]:
        diff = asteroid + stack[-1]
        if diff < 0:
            stack.pop()
        elif diff > 0:
            asteroid = 0
        else:
            asteroid = 0
            stack.pop()

    if asteroid:
        stack.append(asteroid)
print(stack)