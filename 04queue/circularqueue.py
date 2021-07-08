'''
-*- coding: utf-8 -*-
@Author  : zoeyzhu
@Time    : 2021/7/8 1:29 下午
@Software: PyCharm
@File    : circularqueue.py
@function:循环队列实现
入队，tail=tail+1%capicity
出队：head=head+1%capicity
空队：head=tail=0
满=tail+1%capicity=head

'''
from typing import Optional
from itertools import chain
class CircularQueue:
    def __init__(self,capacity):
        self._items = []
        self._capacity=capacity+1
        self._head=0
        self._tail=0
    def enqueue(self,item:str):
        if (self._tail+1)%self._capacity ==self._head:
            return False
        self._items.append(item)
        self._tail=(self._tail+1)%self._capacity
        return True
    def dequeue(self) ->Optional[str]:
        if self._head!=self._tail:
            item=self._items[self._head]
            self._head=(self._head+1)%self._capacity
            return item
    def __repr__(self)->str:
        #循环队列两种情况，head和tail的位置不确定
        if self._tail>=self._head:
            return " ".join(item for item in self._items[self._head:self._tail])
        else:
            return " ".join(item for item in chain(self._items[self._head:], self._items[:self._tail]))


if __name__ == "__main__":
    q = CircularQueue(5)
    for i in range(5):
        q.enqueue(str(i))
    q.dequeue()
    q.dequeue()
    q.enqueue(str(5))
    print(q)