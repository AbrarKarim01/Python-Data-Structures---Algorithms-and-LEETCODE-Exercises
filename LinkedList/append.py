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

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node # if the list is empty, set head and tail to the new node
        else:
            self.tail.next = new_node
            self.tail = new_node # update the tail to the new node

        self.length += 1 # increment the length of the linked list
        return True

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

# Example usage
my_linked_list = LinkedList(4)  # Create a linked list with an initial value of 4
my_linked_list.append(10)  # Append a new value to the linked list
my_linked_list.append(15)  # Append another value
my_linked_list.print_list()  # Print the values in the linked list