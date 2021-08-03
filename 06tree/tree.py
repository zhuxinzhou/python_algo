'''
-*- coding: utf-8 -*-
@Author  : zoeyzhu
@Time    : 2021/8/3 10:30 下午
@Software: PyCharm
@File    : tree.py.py
@function:
实现一个基本的二叉树
'''
from typing import TypeVar, Generic, Generator, Optional


class TreeNode():
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


# Pre-order traversal
def pre_order(root):
    if root:
        print(root.val)
        pre_order(root.left)
        pre_order(root.right)


# In-order traversal
def in_order(root):
    if root:
        in_order(root.left)
        print(root.val)
        in_order(root.right)


# Post-order traversal
def post_order(root):
    if root:
        post_order(root.left)
        post_order(root.right)
        print(  root.val)