#!/bin/python3

"""
 this is a linked list
"""

class Node:
    __slots__ = ("data", "next")
    
    def __init__(self,data):
        self.data = data
        self.next = None

    def show(self):
        head = self
        while head:
            print(head.data)
            head = head.next

    def add(self, element, position):
        head = self
        new_Node = Node(element)
        if position == 1:
            new_node.next = head
            return new_node

        elif:
        
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

n1.next = n2
n2.next = n3

n1.show()
