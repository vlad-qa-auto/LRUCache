from unittest import TestCase

from LRUCache_Dict import LRUCache

cache = LRUCache(3)


class TestLRUCache(TestCase):
    def setUp(self):
        cache.reset()
        cache.put(1, 'v1')
        cache.put(2, 'v2')

    def test_get_value(self):
        self.assertEqual('v1', cache.get(1))

    def test_get_order(self):
        cache.get(1)
        self.assertCache([(2, 'v2'), (1, 'v1')])

    def test_get_none(self):
        self.assertIsNone(cache.get(3))

    def test_put_new(self):
        cache.put(3, 'v3')
        self.assertCache([(1, 'v1'), (2, 'v2'), (3, 'v3')])

    def test_put_exist(self):
        cache.put(1, 'p11')
        self.assertCache([(2, 'v2'), (1, 'p11')])

    def test_put_max(self):
        cache.put(3, 'v3')
        cache.put(4, 'v4')
        self.assertCache([(2, 'v2'), (3, 'v3'), (4, 'v4')])

    def test_delete(self):
        cache.delete(1)
        self.assertCache([(2, 'v2')])

    def test_delete_none(self):
        cache.delete(3)
        self.assertCache([(1, 'v1'), (2, 'v2')])

    def test_reset(self):
        cache.reset()
        self.assertEqual(0, len(cache))
        self.assertEqual(cache.last, cache.first.next)
        self.assertEqual(cache.first, cache.last.prev)

    def assertCache(self, nodes: list) -> None:
        cache_values = list()
        self.assertEqual(nodes[0][0], cache.first.next.key)
        self.assertEqual(nodes[len(nodes) - 1][0], cache.last.prev.key)
        cur = cache.first.next
        while cur.next is not None:
            cache_values.append((cur.key, cur.value))
            cur = cur.next
        self.assertListEqual(nodes, cache_values)
