from collections import deque

senate = "DDRRR"
# R: 0, 3
# D: 1, 2, 4
r_queue = deque()
d_queue = deque()
i = 0

for idx in range(len(senate)):
    if senate[idx] == "R":
        r_queue.append(idx)
    else:
        d_queue.append(idx)

print(d_queue, r_queue)
while d_queue and r_queue:
    dTurn = d_queue.popleft()
    rTurn = r_queue.popleft()
    if rTurn < dTurn:
        r_queue.append(dTurn + len(senate))
    else:
        d_queue.append(rTurn + len(senate))

if r_queue:
    print("Radiant")
elif d_queue:
    print("Dire")