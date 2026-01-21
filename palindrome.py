#!/usr/bin/python3

def palindro(s:str):
    if s == s[::-1]:
        return True
    else:
        return False

