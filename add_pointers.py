#!/bin/python3

def add_two(l1,l2):
    a = []
    b = []

    def turn(l):
        while l:
            a.append(l.data)
            l = l.next
    turn(l1)
    turn(l2)

    print(f"{a} /n {b}")i

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked:
    def __init__(self, start):

