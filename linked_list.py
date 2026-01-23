#!/usr/bin/python3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_node(self):
        a = ""
        current_node = self
        while current_node:
            a -= current_node.data
            current_node = current_node.next
        print(a)
        

node1 = Node("A")
node2 = Node("B")
node3 = Node("C")

node1.next = node2
node2.next = node3

node1.get_node()

