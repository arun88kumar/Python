class Node():
    """
    Node class defines an object in double linked list to maintain the cache
    """
    def __init__(self, key, data):
        self.data = data
        self.key = key
        self.prev = None
        self.nxt = None


class LRUCache():
    def __init__(self, size):
        self.size = size
        self.hash_table = dict()
        self.head = None
        self.end = None

    def __add(self, node):
        """
        Function adds the node to the top of the cache making it as the MRU element
        :param node: the node which needs to be added
        :return: None
        """
        if self.head:
            self.head.prev = node
            node.nxt = self.head
            self.head = node
        else:
            self.head = node
            self.end = node

    def __remove(self, node):
        """
        Function removes the element from cache
        :param node: node which needs to be removed
        :return: None
        """
        if self.head == self.end and self.head == node:
            self.head = None
            self.end = None
        elif self.head == node:
            self.head.nxt.prev = None
            self.head = self.head.nxt
        elif self.end == node:
            self.end.prev.nxt = None
            self.end = self.end.prev
        else:
            node.prev.nxt = node.nxt
            node.nxt.prev = node.prev

    def get(self, key):
        """
        get function - to retrieve the value based on the key
        :param key:
        :return: the data value for the requested key ; None - if key not found
        """
        if key in self.hash_table:
            get_node = self.hash_table[key]
            if self.head == get_node:
                pass
            else:
                self.__remove(get_node)
                self.__add(get_node)
            return get_node.data

    def put(self, key, data):
        """
        Add the key and data to the cache.
        if key already exists , the data is updated and object is made the MRU element
        :param key: key of the data to be added to cache
        :param data: corresponding data object to be added to the cache
        :return: None
        """
        if key in self.hash_table:
            get_node = self.hash_table[key]
            if self.head == get_node:
                pass
            else:
                self.__remove(get_node)
                self.__add(get_node)
            get_node.data = data
            return

        # if Cache size is full, remove the LRU element
        if len(self.hash_table) == self.size:
            del self.hash_table[self.end.key]
            self.__remove(self.end)

        new_node = Node(key, data)
        self.__add(new_node)
        self.hash_table[key] = new_node









