# -*- coding: utf-8 -*-

def binary_to_ten(x):
    n = len(str(x))
    y = 0
    for i in range(n):
        y = y + int(str(x)[i]) * (2**i)
        print(i)
    return y

print(binary_to_ten(1010))
print(bin(25))