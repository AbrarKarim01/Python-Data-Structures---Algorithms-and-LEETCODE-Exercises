class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        # create a new linked list with a head node (constructor)
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def pop(self):
        if self.head is None:
            self.head = None
            self.tail = None  # if the list is empty, set head and tail
        else:
            temp = self.head
            while temp.next is not None:
                prev = temp
                temp = temp.next

            prev.next = None
            self.tail = prev  # update the tail to the previous node
        
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

# Example usage
my_linked_list = LinkedList(4)  # Create a linked list with an initial value of 4
my_linked_list.pop(4)  # Pop a value from the linked list
my_linked_list.print_list()  # Print the values in the linked list