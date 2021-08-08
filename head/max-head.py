'''
-*- coding: utf-8 -*-
@Author  : zoeyzhu
@Time    : 2021/8/8 10:05 下午
@Software: PyCharm
@File    : max-head.py
@function:
实现一个堆
'''

from typing import Optional,List

class Heap:
    def __init__(self,capacity:int):
        self._data=[0]*(capacity+1)
        self._capacity = capacity
        self._count=0
    @classmethod
    def _parent(cls, child_index: int) -> int:
        """The parent index."""
        return child_index // 2
    @classmethod
    def _left(cls,parent_index:int) -> int:
        #为父节点*2
        return parent_index*2
    @classmethod
    def _right(cls,parent_index:int) -> int:
        #为父节点*2+1
        return parent_index*2+1
    def _siftup(self) ->None:
        i,parent=self._count,Heap._parent(self._count)
        while parent and self._data[i]>self._data[parent]:#条件
            self._data[i],self._data[parent]=self._data[parent],self._data[i]#大跟堆
            i,parent=parent,Heap._parent(parent)#网上晒
    @classmethod
    def _siftdown(cls,a:List[int],count:int,root_index:int=1) ->None:
        i=larger_child_index=root_index
        while True:
            left,right=cls._left(i),cls._right(i)
            if left<=count and a[i]<a[left]:
                larger_child_index = left
            if right <= count and a[larger_child_index] < a[right]:
                larger_child_index = right
            if larger_child_index == i:break
            a[i], a[larger_child_index] = a[larger_child_index], a[i]
            i = larger_child_index
    def insert(self,value:int) ->None:
        if self._count>=self._capacity: return
        self._count+=1
        self._data[self._count]=value
        self._siftup()
    def remove_max(self) ->Optional[int]:
        if self._count:
            result=self._data[1]
            self._data[1]=self._data[self._count]
            self._count-=1
            self._siftdown(self._data, self._count)#调整堆
            return result
    @classmethod
    def build_heap(cls,a:List[int]) ->None:
        for i in range((len(a)-1)//2,0,-1):#第三个值是步瓶
            cls._siftdown(a,len(a)-1,i)
    @classmethod
    def sort(cls,a:List[int])->None:
        cls.build_heap(a)
        k=len(a)-1
        while k>1:
            a[1],a[k]=a[k],a[1]
            k-=1
            cls._siftdown(a,k)
if __name__ == "__main__":
    hp = Heap(10)
    hp.insert(3)
    hp.insert(9)
    hp.insert(1)
    hp.insert(8)
    hp.insert(7)
    hp.insert(3)
    print(hp)
    for _ in range(6):
        print(hp.remove_max())
    a = [0, 6, 3, 4, 0, 9, 2, 7, 5, -2, 8, 1, 6, 10]
    Heap.sort(a)
    print(a[1:])



