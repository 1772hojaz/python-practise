#!/bin/python3
import linked_list as l


#*****************LINKED LIST******************#

#_________________Create_______________________#
l1 = l.Linked()
#__________________Insert_______________________#
print("INSERTING ELEMENTS")
l1.append(1)
l1.append(2)
l1.append(3)
l1.append(4)
l1.append(5)
l1.append(6)

print(l1)

#_____________________Search_____________________#




#____________________Remove______________________#

print("REMOVING ELEMENTS")
"Deleting the first Node "

l1.delete(0)
print(f"{l1}\n")

" Deleting a Node that is between two Nodes"
l1.delete(1)
print(f"{l1}\n")

"Deleting the last node"
l1.delete(4)
print(f"{l1}\n")



