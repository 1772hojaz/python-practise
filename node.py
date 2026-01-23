#!/usr/bin/python3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
   
    def get_val(self):
        head = self
        val = []
        while head:
            val.append(head.data)
            head = head.next
        return val
   
    def reverse(self, a):
        return a[::-1]
   
    def tosting(self, a):
        res = ''.join(map(str,a))
        return res
   
    def toint(self, a):
        return int(a)




node1 = Node(1)
node2 = Node(2)
node3 = Node(3)


node1.next = node2
node2.next = node3


# Using Nodes
print((node1.toint(node1.tosting(node1.reverse(node1.get_val())))))

