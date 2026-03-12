#!/bin/python3

class Node:
    __slots__ = ['data', 'next', 'prev']
    def __init__(self,data):
        self.data = data 
        self.next = None
        self.prev = None

class Doubly:
    def __init__(self, head, size):
        self.head = head
        self.size = 0

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

n1.next = n2
n2.prev = n1
n2.next = n3
n3.prev = n2
n3.next = n4
n4.prev = n3

tail = n3
while tail:
    print(f"this is the tail: {tail.data}")
    tail = tail.prev
