#!/usr/bin/python3

input_array = []
with open('input1.txt', 'r') as input:
    line = input.readline()
    while line:
        input_array.append(line.strip())
        line = input.readline()

fuel_array = []
for num in input_array:
    total_fuel = int(num)//3-2
    fuel_fuel = total_fuel//3-2
    while fuel_fuel > 0:
        total_fuel += fuel_fuel
        fuel_fuel = fuel_fuel//3-2

    fuel_array.append(total_fuel)

module_fuel = sum(fuel_array)
print('fuel for modules is ' + str(module_fuel))
