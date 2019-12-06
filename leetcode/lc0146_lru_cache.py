# coding: utf-8
# from: https://leetcode-cn.com/problems/lru-cache/
# keys: hash, double-ll

class Node(object):
    def __init__(self, val, key, prev, next_):
        self.val = val
        self.key = key
        self.next = next_
        self.prev = prev


class LRUCache(object):

    def __init__(self, capacity: int):
        self.head = Node(-1, -1, None, None)
        node = self.head
        for _ in range(capacity - 1):
            new_node = Node(-1, -1, node, None)
            node.next = new_node
            node = new_node

        self.head.prev = node
        node.next = self.head

        self.hash_map = dict()

    def move_to_head(self, cur):
        # A  <->  B  <->  C  <->  D  <-> A
        # head|cur
        #                head

        if self.head == cur:
            self.head = self.head.prev
            return

        # A  <->  B  <->  C  <->  D  <-> A
        # head           cur
        # A  <->  C  <->  B  <->  D  <-> A
        # head   cur
        cur.prev.next = cur.next  # B -> D
        cur.next.prev = cur.prev  # D -> B

        cur.next = self.head.next  # C -> B
        cur.next.prev = cur  # B -> C

        self.head.next = cur  # A -> C
        cur.prev = self.head  # C -> A

    def get(self, key: int) -> int:
        if key not in self.hash_map:
            return -1
        cur = self.hash_map[key]
        self.move_to_head(cur)
        return cur.val

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            cur = self.hash_map[key]
            cur.val = value
            self.move_to_head(cur)
        else:
            if self.head.val != -1:
                del self.hash_map[self.head.key]
            self.head.key = key
            self.head.val = value
            self.hash_map[key] = self.head
            self.head = self.head.prev


if __name__ == '__main__':
    cache = LRUCache(3)
    exit(0)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1

    cache.put(3, 3)
    assert cache.get(2) == -1
    cache.put(4, 4)
    assert cache.get(1) == - 1
    assert cache.get(3) == 3
    assert cache.get(4) == 3
