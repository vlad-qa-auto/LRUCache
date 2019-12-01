class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache(dict):
    def __init__(self, max_size):
        super().__init__()
        self.last = Node(-1, ']')
        self.first = Node(0, '[')
        self.max_size = max_size
        self.reset()

    def get(self, key: int):
        if key not in self:
            return None
        return self.inject(self.withdraw(key)).value

    def put(self, key: int, value: str):
        if key in self:
            self.withdraw(key)
        self[key] = self.inject(Node(key, value))
        if len(self) > self.max_size:
            key = self.first.next.key
            self.withdraw(key)
            self.pop(key)

    def delete(self, key: int):
        if key in self:
            self.withdraw(key)
            self.pop(key)

    def reset(self):
        self.first.next = self.last
        self.last.prev = self.first
        self.clear()

    def withdraw(self, key) -> Node:
        node = self[key]
        node.next.prev = node.prev
        node.prev.next = node.next
        return node

    def inject(self, node) -> Node:
        p = self.last.prev
        p.next = node
        self.last.prev = node
        node.prev = p
        node.next = self.last
        return node
