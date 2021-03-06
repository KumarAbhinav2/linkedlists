"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists.
Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation,
evict the least recently used key.
Follow up:
Could you do get and put in O(1) time complexity?



Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
"""


class DlinkedList:

    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.size = 0
        self.head, self.tail = DlinkedList(), DlinkedList()
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_node(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node):
        prev = node.prev
        new = node.next

        prev.next = new
        new.prev = prev

    def move_to_end(self, node):
        self.remove_node(node)
        self.add_node(node)

    def pop_tail(self):
        curr_tail = self.tail.prev
        self.remove_node(curr_tail)
        return curr_tail

    def get(self, key):
        node = self.cache.get(key, None)

        if not node:
            return -1
        self.move_to_end(node)
        return node.value

    def put(self, key, value):
        node = self.cache.get(key)

        if not node:
            new = DlinkedList()
            new.key = key
            new.value = value
            self.cache[key] = new
            self.add_node(new)
            self.size += 1

            if self.size > self.capacity:
                tail = self.pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            node.value = value
            self.move_to_end(node)


### another python solution
from collections import OrderedDict


class LRUCache2(OrderedDict):

    def __init__(self, capacity):
        self.capacity = capacity

    def get(self, key):
        if key not in self:
            return -1
        self.move_to_end(key)

        return self[key]

    def put(self, key, value):
        if key in self:
            self.move_to_end(key)
        self[key] = value

        if len(self) > self.capacity:
            self.popitem(last=False)
