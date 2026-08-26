#!/bin/python3

"""
SEARCHING PROBLEM

Input:
    A sequence of n numbers

        A = <a1, a2, a3, ..., an>

    and a value v.

Output:
    An index i such that

        v = A[i]

    or the special value NIL if v does not appear in A.
"""

def linear(a, v):
    for i in range(0, len(a)):
        if a[i] == v:
            return i

