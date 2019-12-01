from _collections import OrderedDict
from unittest import TestCase

from LRUCache_OrderedDict import LRUCache

cache = LRUCache(3)


class TestLRUCache(TestCase):
    def setUp(self):
        cache.clear()
        cache[1], cache[2] = 'v1', 'v2'

    def test_get_value(self):
        self.assertEqual('v1', cache.get(1))

    def test_get_order(self):
        cache.get(1)
        self.assertEqual(OrderedDict({2: 'v2', 1: 'v1'}), cache)

    def test_get_none(self):
        self.assertIsNone(cache.get(3))

    def test_put_new(self):
        cache.put(3, 'v3')
        self.assertEqual(OrderedDict({1: 'v1', 2: 'v2', 3: 'v3'}), cache)

    def test_put_exist(self):
        cache.put(1, 'p11')
        self.assertEqual(OrderedDict({2: 'v2', 1: 'p11'}), cache)

    def test_put_max(self):
        cache.put(3, 'v3')
        cache.put(4, 'v4')
        self.assertEqual(OrderedDict({2: 'v2', 3: 'v3', 4: 'v4'}), cache)

    def test_delete(self):
        cache.delete(1)
        self.assertEqual(OrderedDict({2: 'v2'}), cache)

    def test_delete_none(self):
        cache.delete(3)
        self.assertEqual(OrderedDict({1: 'v1', 2: 'v2'}), cache)

    def test_reset(self):
        cache.reset()
        self.assertEqual(OrderedDict(), cache)
