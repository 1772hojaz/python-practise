#!/bin/python3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)


n1.next = n2
n2.next = n3

head = n1
current = head
while current :
    print(current.data)
    current = current.next
    

print("The new list")

tmp = head

while tmp:
    if tmp.next is None:
        tmp.next = Node(4)
        break
    tmp = tmp.next

check = head

while check:
    print(check.data)
    check = check.next


