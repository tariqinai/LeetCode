
gain = [-5, 1, 5, 0, -7]
# gain = [-4,-3,-2,-1,4,3,2]
altitude = 0
max_altitude = 0

for change in gain:
    altitude += change
    max_altitude = max(max_altitude, altitude)

print(max_altitude)
