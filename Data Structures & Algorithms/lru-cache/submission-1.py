class Node:
    def __init__(self, key=None, value=None):
        self.value = value
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # mapping key to the node
        self.head, self.tail = Node(0,0), Node(0,0) # dummy nodes
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert_end(self, node):
        previous = self.tail.prev
        previous.next = node
        node.prev = previous
        node.next = self.tail
        self.tail.prev = node 

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.remove(self.cache[key])
        self.insert_end(self.cache[key])
        return self.cache[key].value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            
        self.cache[key] = Node(key, value)
        self.insert_end(self.cache[key])

        if len(self.cache) > self.capacity:
            node = self.head.next
            self.remove(node)
            del self.cache[node.key]
            

