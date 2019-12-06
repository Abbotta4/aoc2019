#!/usr/bin/python3

import csv
input_array = []
with open('input2.txt', 'r') as input:
    line = input.readline()
ints = list(map(int, line.split(',')))

def crunch(noun, verb):
    buffer = ints.copy()
    buffer[1] = noun
    buffer[2] = verb
    cur = 0
    while True:
        opcode = buffer[cur]
        if opcode is 99:
            break
        else:
            r1 = buffer[buffer[cur + 1]]
            r2 = buffer[buffer[cur + 2]]
            if opcode is 1: # Add
                result = r1 + r2
            if opcode is 2: # Multiply
                result = r1 * r2
            buffer[buffer[cur + 3]] = result
            cur += 4
    return(buffer[0])

for noun in range(100):
    for verb in range(100):
        if crunch(noun, verb) == 19690720:
            print(noun, verb)
            exit(0)
print("couln't find it :(")
