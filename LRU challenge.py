# Enter your code here. Read input from STDIN. Print output to STDOUT
class Node():
    def __init__(self, key, data):
        self.data = data
        self.key = key
        self.prev = None
        self.nxt = None

    def display(self):
        print("{0} {1}".format(self.key, self.data))
        if self.nxt:
            self.nxt.display()

class LRUCache():
    def __init__(self, size):
        self.size = size
        self.hash = dict()
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
            node.next = self.head
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
            self.head.next.prev = None
            self.head = self.head.next
        elif self.end == node:
            self.end.prev.next = None
            self.end = self.end.prev
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

    def get(self, key):
        """
        get function - to retrieve the value based on the key
        :param key:
        :return: the data value for the requested key ; None - if key not found
        """
        if key in self.hash.keys():
            get_node = self.hash[key]
            if self.head == get_node:
                pass
            else:
                self.__remove(get_node)
                self.__add(get_node)
            return get_node.data

    def put(self, key, data):
        """
        Add the key and data to the cache. if key already exists , the data is updated and object is made the MRU element
        :param key: key of the data to be added to cache
        :param data: corresponding data object to be added to the cache
        :return: None
        """
        if key in self.hash.keys():
            get_node = self.hash[key]
            if self.head == get_node:
                pass
            else:
                self.__remove(get_node)
                self.__add(get_node)
            get_node.data = data

        if len(self.hash) >= self.size:
            del self.hash[self.end.key]
            self.__remove(self.end)

        new_node = Node(key, data)
        self.__add(new_node)
        self.hash[key] = new_node
    
    def peek(self,key):
        if key in self.hash.keys():
            return self.hash[key].data

    def lis(self):
        self.head.display()  
   

N = long(raw_input())
cache = None
for _ in range(N):
    cmd = raw_input().split()
    if cmd[0] == "BOUND":
        cache = LRUCache(int(cmd[1]))
    elif cmd[0] == "SET":
        cache.put(cmd[1],cmd[2])
    elif cmd[0] == "GET":
        val = cache.get(cmd[1])
        if val:
            print val
        else:
            print "NULL" 
    elif cmd[0] == "PEEK":
        val = cache.peek(cmd[1])
        if val:
            print val
        else:
            print "NULL"
    elif cmd[0] == "DUMP":
        dump = cache.hash
        for k in sorted(dump.keys()):
            print "{0} {1}".format(k,dump[k].data)
    elif cmd[0] == "LIS":
        cache.lis()
