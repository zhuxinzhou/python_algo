'''
-*- coding: utf-8 -*-
@Author  : zoeyzhu
@Time    : 2021/8/7 10:27 上午
@Software: PyCharm
@File    : bst2.py
@function:
构建一颗二叉搜索数
'''

from typing import List

class TreeNode():
    def __init__(self,value):
        self.val=value
        self.left=None
        self.right=None
class BinarySearchTree():
    def __init__(self):
        self._root=None
    def find(self,value:int):
        node=self._root
        while node and node.val != value:
            node = node.left if node.val > value else node.right
        return node
    def insert(self,value):
        if not self._root:
            self._root=TreeNode(value)
            return
        parent = None
        node=self._root
        while node:
            #node的下一个节点有可能是空节点
            parent=node
            node = node.left if node.val > value else node.right
        new_node = TreeNode(value)
        if parent.val>value:
            parent.left=new_node
        else:
            parent.right=new_node
    def delete(self,value:int):
        node=self._root
        parent=None
        while node and node.val!=value:
            parent=node
            node =node.left if node.val>value else node.right
        if not node:return
        #要删除的节点有两个节点,找到右节点的最小节点
        if node.left and node.right:
            su=node.right
            su_p=node
            while su.left:
                successor_parent = successor
                successor = successor.left
            node.val=su_p.val
            parent,node=successor_parent, successor
        #删除节点是叶子节点，直接删除，
        child = node.left if node.left else node.right
        if not parent:
            self._root=child
        elif parent.left==node:
            parent.left = child
        else:
            parent.right=child