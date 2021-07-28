'''
-*- coding: utf-8 -*-
@Author  : zoeyzhu
@Time    : 2021/7/27 9:37 下午
@Software: PyCharm
@File    : 671.py
@function:
给定一个非空特殊的二叉树，每个节点都是正数，并且每个节点的子节点数量只能为 2 或 0。如果一个节点有两个子节点的话，那么该节点的值等于两个子节点中较小的一个。

更正式地说，root.val = min(root.left.val, root.right.val) 总成立。

给出这样的一个二叉树，你需要输出所有节点中的第二小的值。如果第二小的值不存在的话，输出 -1 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/second-minimum-node-in-a-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import  List


class Solution:
    def __init__(self):
        self.mint=9999
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        key=root
        result=[]
        Solution.travser(root,root.val)
        if self.mint!=root.val and self.mint!=9999:
            return self.mint
        else:
            return -1
        #去重

    def travser(self,tree, key):
        if not tree:
            return
        if tree.val < self.mint and tree.val > key:
            self.mint = tree.val
        Solution.travser(tree.left, key)
        res.append(tree.val)
        Solution.travser(tree.right, key)
