'''
-*- coding: utf-8 -*-
@Author  : zoeyzhu
@Time    : 2021/7/7 2:19 下午
@Software: PyCharm
@File    : link_stack.py
@function:
实现一个链栈
'''
from typing import Optional
class Node:
    def __init__(self,data:int,next=None):
        self._data=data
        self._next=next
class LinkedStack:
    def __init__(self):
        self._top:Node=None
        #栈表初始化，栈首指针初始化
    def push(self,value:int):
        new_top=Node(value)
        new_top._next=self._top
        self._top=new_top
    def pop(self)->Optional[int]:
        if self._top:
            value=self._top._data
            self._top=self._top._next
            return value
    def __repr__(self) ->str:
        current=self._top
        nums=[]
        while current:
            nums.append(current._data)
            current=current._next
        return " ".join(f"{num}" for num in nums)
if __name__ == "__main__":
    stack = LinkedStack()
    for i in range(9):
        stack.push(i)
    print(stack)
    print(stack.__repr__())
    for _ in range(3):
        stack.pop()
    print(stack)