'''
-*- coding: utf-8 -*-
@Author  : zoeyzhu
@Time    : 2021/8/7 11:01 上午
@Software: PyCharm
@File    : red_black_tree.py
@function:
实现一颗红黑树
'''
from queue import Queue
import random

class TreeNode():
    def __init__(self,val=None,color=None):
        self.val=val
        assert color in ['r', 'b']
        self.color = 'red' if color == 'r' else 'black'
        self.left=None
        self.right=None
        self.parent=None
    def is_black(self):
        return self.color == 'black'
    def set_black(self):
        self.color='black'
        return
    def set_red(self):
        self.color='red'
        '''
二、一般的用法是：
assert condition
用来让程序测试这个condition，如果condition为false，那么raise一个AssertionError出来。逻辑上等同于：
if not condition:
    raise AssertionError()
        '''