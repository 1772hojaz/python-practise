#!/bin/python3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0  # helps us validate positions quickly

    def add(self, element, position):
        
        if position < 0 or position > self.size:
            print(f"Invalid position. Must be between 0 and {self.size} (inclusive)")
            return False

        new_node = Node(element)

        
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            self.size += 1
            return True

        

        current = self.head

        
        for _ in range(position - 1):
            current = current.next

        # Now current is the node before insertion point
        new_node.next = current.next
        current.next = new_node
        self.size += 1
        return True

    # Helper method to print the list (for testing)
    def __str__(self):
        if not self.head:
            return "Empty list"
        
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        return " → ".join(result)

    # Optional: add elements at the end for easier testing
    def append(self, element):
        self.add(element, self.size)


# ────────────────────────────────────────────────
# Example usage:
# ────────────────────────────────────────────────

ll = LinkedList()

ll.append(10)     # 10
ll.append(20)     # 10 → 20
ll.append(30)     # 10 → 20 → 30

print("Initial:", ll)          # 10 → 20 → 30

ll.add(5, 0)                   # insert at beginning
print("After add(5, 0):", ll)  # 5 → 10 → 20 → 30

ll.add(15, 2)                  # insert between 10 and 20
print("After add(15, 2):", ll) # 5 → 10 → 15 → 20 → 30

ll.add(99, 5)                  # insert at the end
print("After add(99, 5):", ll) # 5 → 10 → 15 → 20 → 30 → 99

# Invalid positions
ll.add(777, -1)   # should fail
ll.add(777, 10)   # should fail (current size is 6)
