from linkedlist import LinkedList
from node import Node


def delete_from_head(lst):
    first_node = lst.get_head()

    if first_node is not None:
        lst.head_node = first_node.next_node
        first_node.next_node = None
    return True


def deletion_by_value(lst, value):
    if lst.is_empty():
        return
    current_node = lst.get_head()
    prev_node = None
    while current_node is not None:
        if current_node.data == value:
            prev_node.next_node = current_node.next_node
            current_node.next_node = None
        prev_node = current_node
        current_node = current_node.next_node
    return True

lst = LinkedList()
lst.insert_at_head(4)
lst.insert_at_head(10)
lst.insert_at_head(90)
lst.insert_at_head(5)
print(lst.print_list())
deletion_by_value(lst, 10)
print(lst.print_list())
delete_from_head(lst)
print(lst.print_list())
#print(search_in_ll(lst, 4))





