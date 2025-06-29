# class LinkedList:
#     def __init__(self, value):
#         # create a new linked list
#         # create a node
#         pass # pass is used to indicate that this function is not yet implemented

#     def append(self, value):
#         # create a new node
#         # add node to end of the linked list
#         pass

#     def prepend(self, value):
#         # create a new node 
#         # add node to the beginning of the linked list
#         pass

#     def insert(self, index, value):
#         # create a new node
#         # insert node at index
#         pass

# All of them create a new node so we will create a new node class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
              
class LinkedList:
     def __init__(self, value):
        # create a new linked list with a head node
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

my_linked_list = LinkedList(4)  # Create a linked list with an initial value of 10
print(my_linked_list.head.value)  # Access the value of the head node