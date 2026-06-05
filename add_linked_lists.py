#!/bin/python3

def add_two(l1,l2):
# tying to thing about this problem

    def turn(l):
        a = []
        while l:
            a.append(l.data)
            l = l.next
        a = a[::-1]
        
        return "".join(map(str,a))

    x = int(turn(l1))
    y = int(turn(l2))


    print(f"{x} and  {y}")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

n0 = Node(0)
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

n0.next = n1
n1.next = n2
n2.next = n3

x1 = Node(9)
x2 = Node(8)
x3 = Node(7)
x4 = Node(6)

x1.next = x2
x2.next = x3
x3.next = x4

add_two(x1,n0)
