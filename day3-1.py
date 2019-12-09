#!/usr/bin/python3

wires = []
with open('input3.txt', 'r') as input:
    line = input.readline()
    while line:
        wires.append(line.strip())
        line = input.readline()

directions = [None, None]
wire_coords = [None, None]

for wire in range(2): # two wires
    wire_coords[wire] = []
    directions[wire] = wires[wire].split(',')
    wire_coords[wire].append([0,0]) # [0,0] arbitrarily chosen as "central port"
    for direction in directions[wire]:
        length = int(direction[1:])
        standing = wire_coords[wire][-1]
        for segment in range(1, length + 1):
            if direction[0] is 'U':
                wire_coords[wire].append([standing[0], standing[1] + segment])
            if direction[0] is 'D':
                wire_coords[wire].append([standing[0], standing[1] - segment])
            if direction[0] is 'L':
                wire_coords[wire].append([standing[0] - segment, standing[1]])
            if direction[0] is 'R':
                wire_coords[wire].append([standing[0] + segment, standing[1]])

def sortAbs(val):
    return abs(val[0]) + abs(val[1])

                
wire_coords[0].sort(key=sortAbs)
wire_coords[1].sort(key=sortAbs)
gener = (x for x in wire_coords[0] if x in wire_coords[1])
next(gener) # Throw out first [0,0] value
result = next(gener, None)
print("Part 1:", abs(result[0]) + abs(result[1]))
