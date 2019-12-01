import collections


class LRUCache(collections.OrderedDict):

    def __init__(self, max_size: int):
        super().__init__()
        self.max_size = max_size

    def get(self, key: int):
        if key not in self.keys():
            return None
        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: str) -> None:
        self.pop(key, None)
        self[key] = value
        if len(self) > self.max_size:
            self.popitem(last=False)

    def delete(self, key: int):
        self.pop(key, None)

    def reset(self):
        self.clear()
