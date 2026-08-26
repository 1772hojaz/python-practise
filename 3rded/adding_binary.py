#!/bin/python3

# adding bit-binary integers stored in two arrays

def add(a, b):
        result = []
        carry = 0
        i = len(a)-1
        while i >= 0:
            x = a[i] + b[i] + carry
            result.append(x%2)
            carry = x//2
            i-=1
            
        return result[::-1]
