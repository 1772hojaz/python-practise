#!/bin/python

a = [5,2,4,6,1,3]

def insert(arr):
    for j in range(0, len(arr)):
        key = arr[j]
    #Insert A[j] into the sorted sequence A[a,..j-1].
        i = j-1

        while i >= 0 and arr[i] > key:
            arr[i+1] = arr[i]
            i -= 1
            arr[i+1] = key

    return arr

print(insert(a))
