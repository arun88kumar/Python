import unittest
from LRU import LRUCache
from random import randint
import sys


sys.setrecursionlimit(5000)
print(sys.getrecursionlimit())
simple_cache = []
simple_cache_length = 500
cache = LRUCache(simple_cache_length)
cache_list = []


def square(n):
    return n * n


def fetch(n):
    val = cache.get(n)
    if not val:
        val = square(n)
        cache.put(n, val)
        global simple_cache
        simple_cache.insert(0, n)
        if len(simple_cache) >= simple_cache_length:
            simple_cache = simple_cache[:simple_cache_length]
    else:
        simple_cache.remove(n)
        simple_cache.insert(0, n)
    return val


def create_cache(node):
    cache_list.append(node.key)
    if node.nxt:
        create_cache(node.nxt)


def validate():
    cache_list = []
    create_cache(cache.head)
    s = [i for i, j in zip(cache_list, simple_cache) if i != j]
    if len(s) > 0:
        print("difference in item")
        print(cache_list)
        print(cache.hash_table)
        print(simple_cache)
        return False

    s = [i for i in simple_cache if i not in cache.hash_table.keys()]
    if len(s) > 0:
        print("difference in hash table")
        print(cache_list)
        print(cache.hash_table)
        print(simple_cache)
        return False

    s = [i for i in cache.hash_table if i not in simple_cache]
    if len(s) > 0:
        print("difference in hash table")
        print(cache_list)
        print(cache.hash_table)
        print(simple_cache)
        return False

    if cache.head.key != simple_cache[0]:
        print("head not equal")
        print(cache.head.key)
        print(cache_list)
        print(cache.hash_table)
        print(simple_cache)
        return False

    if cache.end.key != simple_cache[-1]:
        print("end not equal")
        print(cache.end.key)
        print(cache_list)
        print(cache.hash_table)
        print(simple_cache)
        return False

    return True


class LRU_testcase(unittest.TestCase):
    def test_1(self):
        for i in range(100000):
            fetch(randint(1, 10000))
            val = validate()
            try:
                self.assertTrue(val)
            except AssertionError:
                print("i"+str(i))
                raise



if __name__ == "__main__":
    unittest.main()
