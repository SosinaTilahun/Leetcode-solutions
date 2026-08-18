class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

        # Dummy nodes
        self.left = Node()
        self.right = Node()

        self.left.next = self.right
        self.right.prev = self.left

    # Remove a node from the linked list
    def remove(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    # Insert a node right before the right dummy node
    # This means it becomes the most recently used
    def insert(self, node):
        prev_node = self.right.prev
        next_node = self.right

        prev_node.next = node
        node.prev = prev_node

        node.next = next_node
        next_node.prev = node

    def get(self, key):
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # Move it to the most recently used position
        self.remove(node)
        self.insert(node)

        return node.value

    def put(self, key, value):
        if key in self.cache:
            # Remove the old node
            self.remove(self.cache[key])

        # Create the new/updated node
        node = Node(key, value)

        # Store it in the hash map
        self.cache[key] = node

        # Add it as most recently used
        self.insert(node)

        # If capacity is exceeded
        if len(self.cache) > self.capacity:
            # Least recently used node
            lru = self.left.next

            self.remove(lru)
            del self.cache[lru.key]