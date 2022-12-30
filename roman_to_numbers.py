#!/usr/bin/env python3
def roman_converter(s):
    ints = (1000, 900,  500, 400, 100, 50, 10,  9,   5,  4,   1)
    rom = ('M',  'CM', 'D', 'CD','C','L','X','IX','V','IV','I')
    result = []
    for i in range(len(ints)):
        count = int(s/ints[i])
        result.append(rom[i]*count)
        s-=ints[i] * count
    return ''.join(result)

print(roman_converter(99))