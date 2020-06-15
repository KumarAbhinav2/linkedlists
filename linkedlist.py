from node import Node


class LinkedList:

    def __init__(self):
        self.head_node = None

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next_node = self.get_head()
        self.head_node = new_node
        return self.head_node

    def is_empty(self):
        if not self.head_node:
            return True
        return False

    def get_head(self):
        return self.head_node

    def print_list(self):
        if self.is_empty():
            print("List is Empty")
            return None
        temp_node = self.get_head()
        while temp_node.next_node is not None:
            print(temp_node.data, end='->')
            temp_node = temp_node.next_node
        print(temp_node.data, "-> None")
        return True