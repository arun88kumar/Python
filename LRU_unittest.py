import unittest
from LRU import LRUCache


class LRUCacheCheck(LRUCache):
    def __init__(self, size):
        super(LRUCacheCheck, self).__init__(size)

    def validate(self, h, e, l):
        if self.head.key != h:
            print('head')
            return False

        if self.end.key != e:
            print('end')
            return False

        L = list()

        def retrieve(node):
            L.append(node.key)
            if not node.nxt:
                retrieve(node.nxt)

        retrieve(self.head)
        result = [i for i, j in zip(L, l) if i != j]

        if len(result) > 0:
            print("list wrong")
            return False







class LRU_testcase2(unittest.TestCase):
    def setUp(self):
        self.cache = LRUCache(5)

    def test_get_1(self):
        val = self.cache.get(1)
        self.assertEqual(val, None)

    def test_put_1(self):
        val = self.cache.get(1)
        self.assertEqual(val, None)
        self.cache.put(1, "abc")
        self.cache.put(2, "abce")
        val = self.cache.get(1)
        self.assertEqual(val, "abc")
        #self.cache.put(2, "abcd")
        print(self.cache.head.key)
        print(self.cache.head.nxt.key)
        print(self.cache.end.key)



if __name__ == "__main__":
    unittest.main()
