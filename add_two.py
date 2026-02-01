#!/bin/python3
from typig import Optional

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:

    def add(self, l1:Optional[Node], l2:Optional[Node] -> Optional[Node]):
        a = []
        b = []
        #extract values from the nodes
        while l1:
            #put them in a list
            a.append(l1.val)
            l1 = l1.next
        while l2:
            b.append(l2.val)
            l2 = l2.next

        # change the list into  a string 
        # change the string into an int

        #add the two integers
        result  = int(''.join(map(str,a[::-1]))) + int(''.join(map(str, b[::-1])))

        # finaly change the reverse the list and change into a linked list

        final = list(str(result)[::-1])

        head = None
        currect = None

        for value in final:
            node = Node(int(value))
            if head is None:
                head = node
                current = node
            else:
                current.next = node 
                current = node

        return head
