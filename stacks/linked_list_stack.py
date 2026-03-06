#!/bin/python3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def pop_l(self):
        pass


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)


n1.next = n2
n2.next = n3


while n1 :
    print(n1.data)
    n1 = n1.next
