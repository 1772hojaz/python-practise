#!/bin/python3

class Node:
    __slots__ = ['data', 'next', 'prev']
    def __init__(self,data):
        self.data = data 
        self.next = None
        self.prev = None

class Doubly:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, position, value):
        
        if position < 0 or position > self.size:
            print(f"Invalid position value:the position must be > 0 and < {self.size}")
            return 0

        elif position == 0:
            new_node = Node(value)
            current = self.head

            self.head = new_node
            new_node.next = current
            self.size += 1
            return 1
        else:
            new_node = Node(value)
            current = self.head
            
            for i in range(position - 1):
                current = current.next
                i += 1
            current.next = new_node.next
            current.next = new_node
            self.size += 1

            return 1



    def __str__(self):
        a = []
        current = self.head

        while current:
            a.append(current.data)
            current = current.next
        
        return f"{a}" 

    def add(self, value):
        self.insert(self.size, value)
        return 1

