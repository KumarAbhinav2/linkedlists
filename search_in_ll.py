"""
Search an element in singly linked list
Linked List = 5->90->10->4
Integer = 4

output = True
"""
from node import Node
from linkedlist import LinkedList


def search_in_ll(lst, value):
    current_node = Node(value)
    while current_node:
        if current_node.data is value:
            return True
        current_node = current_node.next_node
    return False

lst = LinkedList()
lst.insert_at_head(4)
lst.insert_at_head(10)
lst.insert_at_head(90)
lst.insert_at_head(5)
#print(lst.print_list())
print(search_in_ll(lst, 4))