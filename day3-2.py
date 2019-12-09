#!/usr/bin/python3

wires = []
with open("input3.txt", 'r') as input:
    line = input.readline()
    while line:
        wires.append(line.strip())
        line = input.readline()

directions = [None, None]
wire_coords = [None, None]
wire_coords_d = [None, None]

for wire in range(2): # two wires
    wire_coords[wire] = []
    wire_coords_d[wire] = {}
    directions[wire] = wires[wire].split(',')
    wire_coords[wire].append([0,0,0]) # [0,0] arbitrarily chosen as "central port," 0 starting length
    wire_coords_d[wire][str([0, 0])] = 0  # maintain a dictionary as well for part 2
    for direction in directions[wire]:
        length = int(direction[1:])
        standing = wire_coords[wire][-1]
        for segment in range(1, length + 1):
            if direction[0] is 'U':
                wire_coords_d[wire][str([standing[0], standing[1] + segment])] = standing[2] + segment
                wire_coords[wire].append([standing[0], standing[1] + segment, standing[2] + segment])
            if direction[0] is 'D':
                wire_coords_d[wire][str([standing[0], standing[1] - segment])] = standing[2] + segment
                wire_coords[wire].append([standing[0], standing[1] - segment, standing[2] + segment])
            if direction[0] is 'L':
                wire_coords_d[wire][str([standing[0] - segment, standing[1]])] = standing[2] + segment
                wire_coords[wire].append([standing[0] - segment, standing[1], standing[2] + segment])
            if direction[0] is 'R':
                wire_coords_d[wire][str([standing[0] + segment, standing[1]])] = standing[2] + segment
                wire_coords[wire].append([standing[0] + segment, standing[1], standing[2] + segment])

def sortLength(val):
    return val[1]

keys = [x for x in wire_coords_d[0].keys() if x in wire_coords_d[1].keys()]
combined = []
for key in keys:
    result = [key]
    result.append(wire_coords_d[0][key] + wire_coords_d[1][key])
    combined.append(result)
combined.sort(key=sortLength)
print("Part 2:", combined[1][1])
