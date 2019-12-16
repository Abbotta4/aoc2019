#!/usr/bin/python3

input_array = []
with open('input5.txt', 'r') as inp:
    line = inp.readline()
ints = list(map(int, line.split(',')))

final_out = None

def crunch(system_id, final_out):
    buffer = ints.copy()
    inp = system_id
    cur = 0
    while True:
        instruction = buffer[cur]
        opcode = str(instruction).zfill(4)[-2:]
        if opcode == '99':
            break
        elif opcode in ('03', '04', '05', '06'): # one parameter
            loc = cur + 1 if int(str(instruction).zfill(4)[-3]) else buffer[cur + 1]
            dst = cur + 2 if int(str(instruction).zfill(4)[-4]) else buffer[cur + 2]
            if opcode == '03': # input
                buffer[loc] = inp
                cur += 2
            elif opcode == '04': # output
                final_out = buffer[loc]
                print("opcode 4: output is", final_out)
                cur += 2
            elif opcode == '05': # jump-if-true
                if buffer[loc] != 0:
                    cur = buffer[dst]
                else:
                    cur += 3
            elif opcode == '06': # jump-if-false
                if buffer[loc] == 0:
                    cur = buffer[dst]
                else:
                    cur += 3
            else: # Error
                print("Something went wrong")
                exit(1)
        else: # two parameters
            r1 = buffer[cur + 1] if int(str(instruction).zfill(4)[-3]) else buffer[buffer[cur + 1]]
            r2 = buffer[cur + 2] if int(str(instruction).zfill(4)[-4]) else buffer[buffer[cur + 2]]
            if opcode == '01': # add
                result = r1 + r2
            if opcode == '02': # multiply
                result = r1 * r2
            if opcode == '07': # less than
                result = 1 if r1 < r2 else 0
            if opcode == '08': # equals
                result = 1 if r1 == r2 else 0
            buffer[buffer[cur + 3]] = result
            cur += 4
    return(final_out)

print("final_out is", crunch(5, final_out))
