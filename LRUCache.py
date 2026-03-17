# Time Complexity : O(1) for both get and put
# Space Complexity : O(capacity) for storing up to capacity items in map and linked list
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No
# Approach : We store each key’s node in a map so we can find it instantly.
# We use a doubly linked list to track usage order, moving items to the front when used.
# When we're full, we throw out the least-used item from the back of the list.

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def insertAtStart(self, node):
        temp = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = temp
        temp.prev = node

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None        

    def get(self, key: int) -> int:
        if key in self.dic:
            node = self.dic[key]
            self.removeNode(node)
            self.insertAtStart(node)
            return node.val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            node = self.dic[key]
            node.val = value
            self.removeNode(node)
            self.insertAtStart(node)
        else:
            node = Node(key, value)
            self.dic[key] = node
            self.insertAtStart(node)
            if len(self.dic) > self.capacity:
                node = self.tail.prev
                self.dic.pop(node.key)
                self.removeNode(node)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)