class Node:
    """ Represents an item for LRU-cache. Contains @key, @value and links to previous and next items in the cache. """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache(dict):
    """ Least-Recently Used Cache stores a limited count of items (defined as @max_size).
        Items are sorted by time of usage.
        Discards the least-recently used item if cache if full.
    """

    def __init__(self, max_size: int):
        super().__init__()
        self.first = Node('first', 'first')  # Dummy first node. Not in cache, just for links.
        self.last = Node('last', 'last')  # Dummy last node. Not in cache, just for links.
        self.max_size = max_size
        self.reset()

    def get(self, key):
        """ Returns the value of cache item by @key.
            Makes item the most-recently used.
            Returns None if cache does not contain @key.
        """
        if key not in self:
            return None
        return self._link_to_end(self._withdraw(key)).value

    def put(self, key, value):
        """ Puts new item to cache.
            If @key is already in cache, updates @value and makes item the most-recently used.
            Discards the least-recently used item if cache if full.
        """
        if key in self:
            self._withdraw(key)
        self[key] = self._link_to_end(Node(key, value))
        if len(self) > self.max_size:
            key = self.first.next.key
            self._withdraw(key)
            self.pop(key)

    def delete(self, key):
        """ Deletes item from cache. """
        if key in self:
            self._withdraw(key)
            self.pop(key)

    def reset(self):
        """ Restores cache to initial state. Removes all nodes. """
        self.first.next = self.last
        self.last.prev = self.first
        self.clear()

    def _withdraw(self, key) -> Node:
        """ Withdraws node from queue by manipulating the links.
            Does not change cache. Does not change @key and value of node. Returns the withdrawn node.
        """
        node = self[key]
        node.next.prev = node.prev
        node.prev.next = node.next
        return node

    def _link_to_end(self, node) -> Node:
        """ Links @node to the end of queue and returns this node. Changes just links.
            Does not change cache. Does not change key and value of node. Returns the linked node.
        """
        p = self.last.prev
        p.next = node
        self.last.prev = node
        node.prev = p
        node.next = self.last
        return node
