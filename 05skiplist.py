'''
-*- coding: utf-8 -*-
@Author  : zoeyzhu
@Time    : 2021/7/29 11:35 下午
@Software: PyCharm
@File    : 05skiplist.py
@function:
实现一个跳表
'''
from typing import Optional
import random
class ListNode:
    def __init__(self,data:Optional[int] =None):
        self._data=data
        self._forwards=[]#下一层
class SkipList:
    _MAX_LEVEL=16

    def __init__(self):
        self.level_count=1
        self._head=ListNode()
        self._head._forwards=[None]*type(self)._MAX_LEVEL
    def find(self,value:int):
        p=self._head
        for i in range(self.level_count-1,-1,-1):
            while p._forwards[i] and p._forwards[i]._data < value:
                p = p._forwards[i]
            return p._forwards[0] if p._forwards[0] and p._forwards[0]._data == value else None

    def insert(self, value: int):
        level = self._random_level()
        if self._level_count < level: self._level_count = level
        new_node = ListNode(value)
        new_node._forwards = [None] * level
        update = [self._head] * level  # update is like a list of prevs

        p = self._head
        for i in range(level - 1, -1, -1):
            while p._forwards[i] and p._forwards[i]._data < value:
                p = p._forwards[i]

            update[i] = p  # Found a prev

        for i in range(level):
            new_node._forwards[i] = update[i]._forwards[i]  # new_node.next = prev.next
            update[i]._forwards[i] = new_node  # prev.next = new_node

