class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        # Dummy nodes
        self.left = ListNode(0, 0)
        self.right = ListNode(0, 0)

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev

    def insert(self, node):
        prev = self.right.prev
        next = self.right

        prev.next = node
        node.prev = prev

        node.next = next
        next.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # Move to MRU
        self.remove(node)
        self.insert(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Remove old node
            self.remove(self.cache[key])

        # Create new node
        node = ListNode(key, value)

        # Store in hashmap
        self.cache[key] = node

        # Put at MRU position
        self.insert(node)

        # Too many items
        if len(self.cache) > self.capacity:
            # LRU node
            lru = self.left.next

            self.remove(lru)

            del self.cache[lru.key]