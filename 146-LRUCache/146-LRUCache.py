// Last updated: 3/19/2025, 3:08:51 PM
class ListNode:
    def __init__(self, key = None, val = None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.key_to_node = {}
        
    def add(self, node):
        # add to beginning
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def remove(self, node):
        prv, nxt = node.prev, node.next
        prv.next = nxt
        nxt.prev = prv

        # remove node directly

    def get(self, key: int) -> int:
        if key in self.key_to_node:
            curr_node = self.key_to_node[key]
            self.remove(curr_node)
            self.add(curr_node)
            return curr_node.val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            original_node = self.key_to_node[key]
            new_node = ListNode(key=key, val=value)
            self.key_to_node[key] = new_node
            self.remove(original_node)
            self.add(new_node)
        else:
            new_node = ListNode(key=key, val=value)
            self.key_to_node[key] = new_node
            if len(self.key_to_node) > self.capacity:
                last_node = self.tail.prev
                self.remove(last_node)
                del self.key_to_node[last_node.key]
            self.add(new_node)

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)