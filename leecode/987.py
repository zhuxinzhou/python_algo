'''
-*- coding: utf-8 -*-
@Author  : zoeyzhu
@Time    : 2021/7/31 10:12 下午
@Software: PyCharm
@File    : 987.py
@function:
给你二叉树的根结点 root ，请你设计算法计算二叉树的 垂序遍历 序列。

对位于 (row, col) 的每个结点而言，其左右子结点分别位于 (row + 1, col - 1) 和 (row + 1, col + 1) 。树的根结点位于 (0, 0) 。

二叉树的 垂序遍历 从最左边的列开始直到最右边的列结束，按列索引每一列上的所有结点，形成一个按出现位置从上到下排序的有序列表。如果同行同列上有多个结点，则按结点的值从小到大进行排序。

返回二叉树的 垂序遍历 序列。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/vertical-order-traversal-of-a-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
import functools
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.res=[]
        self.dictr=[]
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        Solution.tarverse(self,root,0,0)
        print(self.dictr)
        # self.dictr.sort(key=functools.cmp_to_key(cmpx))
        a=dict()
        self.dictr.sort()
        for item in self.dictr:
            if item[2] in a.keys():
                a[item[2]].append(item[0].val)
            else:
                _tm=[item[0].val]
                a[item[2]]=_tm

        for item in a.keys():
            self.res.append(a[item])
        return self.res

    def tarverse(self,tree,x,y):
        if not tree:
            return
        _tem=[y,x,tree]
        self.dictr.append(_tem)
        Solution.tarverse(self,tree.left,x+1,y-1)
        Solution.tarverse(self,tree.right,x+1,y+1)


tem=[['A',0,0],['B',0,-1]]

def cmpx(x,y):
    if x[2]==y[2]:
        return x[1]-y[1]
    else:
        return x[2]-y[2]





print(chance_sort(tem))

