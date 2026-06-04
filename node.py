#!/bin/python3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


n1 = Node(12)
n2 = Node(13)
n3 = Node(14)

n1.next = n2
n2.next = n3

while n1:
    print(f"the value is {n1.data}")
    n1 = n1.next
