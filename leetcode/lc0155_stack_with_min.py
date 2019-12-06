# coding: utf-8
# from: https://leetcode-cn.com/problems/min-stack/
# keys: stack

import sys


class MinStack(object):

    def __init__(self):
        self.min = list()
        self.main = list()

    def push(self, val):
        # O(1)
        self.main.append(val)
        if not self.min or val < self.min[-1]:
            self.min.append(val)

    def pop(self):
        val = self.main.pop()
        if self.min and val == self.min[-1]:
            self.min.pop()
        return val

    def top(self):
        if self.main:
            return self.main[-1]
        return None

    def get_min(self):
        if self.min:
            return self.min[-1]
        return None


class MinStack2(object):

    def __init__(self):
        self.min = sys.maxsize
        self.main = list()

    def push(self, val):
        if val <= self.min:
            self.main.append(self.min)
            self.min = val

        self.main.append(val)

    def pop(self):
        if not self.main:
            return None

        val = self.main.pop()
        if val == self.min:
            val = self.main.pop()
            self.min = val

        return val

    def top(self):
        if self.main:
            return self.main[-1]
        return None

    def get_min(self):
        return self.min


if __name__ == '__main__':

    def test(s):
        s.push(-2)
        s.push(0)
        s.push(-3)
        assert -3 == s.get_min()
        s.pop()
        assert 0 == s.top()
        assert -2 == s.get_min()

    stack = MinStack()
    test(stack)

    stack2 = MinStack2()
    test(stack2)

