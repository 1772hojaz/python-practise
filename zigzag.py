#!/usr/bin/python3

def zigzag(numbers):
    n = numbers
    a = []
    for i in range(0, len(n)-1,2):
        if n[i] < n[i+1]:
            a.append(1)
    return(a)

n = [3, 6, 1, 5, 2]

print(f"{zigzag(n)}")

