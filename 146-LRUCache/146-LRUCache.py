// Last updated: 3/4/2025, 1:09:45 PM
class ListNode:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.key_to_node = {}

    def add(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.key_to_node:
            node = self.key_to_node[key]
            self.remove(node) # remove from DLL
            self.add(node) # Add to beginning
            return node.val
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        
        if key in self.key_to_node:
            node = self.key_to_node[key]
            self.remove(node)

        new_node = ListNode(key, value)
        self.add(new_node)
        self.key_to_node[key] = new_node
        if len(self.key_to_node) > self.capacity:
            last_node = self.tail.prev
            self.remove(last_node)
            del self.key_to_node[last_node.key]

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)