"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
from linked_lists import Node, LinkedList

 # Using arrays
class ArrStack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        self.size = len(self.storage)
        return self.size

    def push(self, value):
         self.storage.append(value)

    def pop(self):
         if len(self.storage) is not 0:
             return self.storage.pop(-1)
         return None

# Using linked list
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size
        

    def push(self, value):
        self.size += 1
        self.storage.add_to_head(value)

    def pop(self):
        if self.size is not 0:
         self.size -= 1
         return self.storage.remove_from_head()
