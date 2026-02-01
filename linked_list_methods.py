#!/usr/bin/python3

"""
In this file I will perform linked list operations starting with Insertion
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def show(node):
    while node is not None:
        print(f"{node.data}", end="")
        node = node.next
        if node is not None:
            print(f"->", end="")
    print()


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next = node3
show(node1)


node7 = Node(7)


node7.next = node1

show(node7)

