import collections


class LRUCache(collections.OrderedDict):
    """ Least-Recently Used Cache stores a limited count of items (defined as @max_size).
        Items are sorted by time of usage.
        Discards the least-recently used item if cache if full.
    """

    def __init__(self, max_size: int):
        super().__init__()
        self.max_size = max_size

    def get(self, key):
        """ Returns the value of cache item by @key.
            Makes item the most-recently used.
            Returns None if cache does not contain @key.
        """
        if key not in self.keys():
            return None
        self.move_to_end(key)
        return self[key]

    def put(self, key, value) -> None:
        """ Puts new item to cache.
            If @key is already in cache, updates @value and makes item the most-recently used.
            Discards the least-recently used item if cache if full.
        """
        self.pop(key, None)
        self[key] = value
        if len(self) > self.max_size:
            self.popitem(last=False)

    def delete(self, key):
        """ Deletes item from cache. """
        self.pop(key, None)

    def reset(self):
        """ Restores cache to initial state. Removes all nodes. """
        self.clear()
