#!/bin/python

a = [5,2,4,6,1,3]

#sort this using insertion sorting

def insertsort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        # the key holds the potato value in my hand
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i+1] = arr[i]
            i -= 1
            arr[i+1] = key
    return arr
print(insertsort(a))
