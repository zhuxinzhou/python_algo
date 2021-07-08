'''
-*- coding: utf-8 -*-
@Author  : zoeyzhu
@Time    : 2021/7/7 7:39 下午
@Software: PyCharm
@File    : arrayQueue.py
@function:
顺序队列，用list实现队列
'''
from typing import Optional
class ArrayQueue:
    def __init__(self,capacity:int):
        self._items=[]
        self._capacity=capacity
        self._head=0
        self._tail=0
    def enqueue(self,item:str) -> bool:
        if self._tail == self._capacity:##队满
            if self._head==0:
                return False
            else: ##，假满了
                for i in range(0,self._tail-self._head):
                    self._items[i]=self._items[i+self._head]
                self._tail=self._tail-self._head#搬移操作，画个图就明白，https://upload-images.jianshu.io/upload_images/16487280-da17f7b4a41271d9.png?imageMogr2/auto-orient/strip|imageView2/2/w/1142/format/webp
                self._head=0
        self._items.insert(self._tail, item)
        self._tail += 1
        return True
    def dequeue(self) -> Optional[str]:
        if self._head != self._tail:
            item = self._items[self._head]
            self._head += 1# 往前
            return item
        else:
            return None

    def __repr__(self) -> str:
        return " ".join(str(item) for item in self._items[self._head: self._tail])#输入方式
    def print(self):
        for item in self._items[self._head:self._tail]:
            print(item)
        print("->".join(str(item) for item in self._items[self._head:self._tail]))

if __name__=='__main__':
    queue=ArrayQueue(5)
    for i in range(0,5):
        queue.enqueue(i)

    queue.print()
    print(queue.__repr__())
