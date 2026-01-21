#!/usr/bin/python3
"""
    from year 0 to 100 that the 1st century
    and from 101 to 200 thats the 2nd cedntury

"""
def century(num):
    if num == 0:
        return 1

    elif num % 100 != 0:
        return ( (num // 100) + 1)
    else:
        return (num // 100)


