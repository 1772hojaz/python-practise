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
            print(f" -> ", end="")
    print()


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

show(head) # The first linked list (1 -> 2 -> 3)

#INputing at the end of a linkedlist

def insertAtEnd(head, x):
    
    new = Node(x)
    last = head


    while last.next is not None:
        last = last.next

    last.next = new

    return head


a = insertAtEnd(head, 5)

show(a)



