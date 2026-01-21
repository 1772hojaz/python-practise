#!/usr/bin/python3

def no_c(my_string):
    for i in range(0, len(my_string), 1):
        if my_string[i] == 'c' or my_string[i] == 'C':
            del my_string[i]
            
    return my_string

