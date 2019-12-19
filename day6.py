#!/usr/bin/python3

orbits = {}
with open('input6.txt', 'r') as input:
    line = input.readline()
    while line:
        split = line.split(')')
        if split[0] not in orbits.keys():
            orbits[split[0]] = []
        orbits[split[0]].append(split[1].strip())
        line = input.readline()

count = 0
def sum_depths(root, depth):
    global count
    for orbit in root:
        count += depth + 1
        if orbit in orbits.keys():
            sum_depths(orbits[orbit], depth + 1)

num_orbits = sum_depths(orbits['COM'], 0) # Center of Mass as starting point
print('number of orbits is', count)
