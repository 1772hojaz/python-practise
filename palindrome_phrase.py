#!/usr/bin/python3

def phrase(s:str):
    a = ""
    s = s.casefold()
    for char in s:
        int_value = ord(char)
        
        if 97 <= int_value <= 122 or 48 <= int_value <= 57:
            a += chr(int_value)
    if a == a[::-1]:
        print(f"{True} {a}")
    else:
        print(f"{False} {a}")

phrase("A man, a plan, a canal: Panama\n")
phrase("101\n")
phrase("0P")
