#!/bin/python3

"""
 this is a linked list
"""

class Node:
    __slots__ = ("data", "next")
    
    def __init__(self,data):
        self.data = data
        self.next = None

class Linked:
    def __init__(self):
        self.head = None
        self.size = 0

    def add(self, position, element):
        if position < 0:
            print("position of the element should be greater than 0")
            return False

        elif position > self.size:
            print(f"position of the element should be less than {self.size}")
            return False

        elif position == 0:
            current = self.head

            self.head = Node(element)

            self.head.next = current

            self.size += 1

            return True

        else:
            current = self.head
            new_node = Node(element)

            for i in range(position-1):
                current = current.next
                i += 1

            new_node.next = current.next
            current.next = new_node
            self.size += 1

            return True
                


    def __str__(self):

        my_list = []

        current = self.head

        while current:
            my_list.append(str(current.data))
            current = current.next

        return "->".join(my_list)

    def append(self, element):
        self.add(self.size, element)
        return True



l1 = Linked()

l1.append(10)
l1.append(20)
l1.append(30)

l1.add(0,90)
l1.add(3,500)
print(l1)
