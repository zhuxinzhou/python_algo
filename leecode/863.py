'''
-*- coding: utf-8 -*-
@Author  : zoeyzhu
@Time    : 2021/7/28 8:08 下午
@Software: PyCharm
@File    : 863.py
@function:
给定一个二叉树（具有根结点 root）， 一个目标结点 target ，和一个整数值 K 。

返回到目标结点 target 距离为 K 的所有结点的值的列表。 答案可以以任何顺序返回。

 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/all-nodes-distance-k-in-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def __init__(self):
        self.dis=0
        self.dts=0
        self.res=[]
        self.ftnode=[]
        self.dislist=dict()
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        #dis[target][node]=dis[target][father]+1
        #该节点后的节点
        Solution.dfs(self,target,k)
        #该节点前的节点
        Solution.find_before(self,root,target)
        Solution.get_res(self,target,k,target)
        return self.res

    def dfs(self, node, key):
        if not node:
            return
        self.dis = self.dis + 1
        if self.dis == key + 1:
            self.res.append(node.val)
            return
        if self.dis >= key + 1:
            return
        Solution.dfs(self, node.left, key)
        Solution.dfs(self, node.right, key)

    def find_before(self,node,target):
        if not node:
            return
        self.dts=self.dts+1
        self.dislist[node]=self.dts-1
        if node ==target:
            return
        if node.left:
            self.ftnode[node.left]=[node,0]
        if node.right:
            self.ftnode[node.right] = [node,1]
        self.find_before(self,node.left,target)
        self.find_before(self,node.right,target)


    def get_res(self,target,k,node):
         if target not in self.ftnode:
             return
         node =self.ftnode[node]
         self.dts=self.dts+1
         dis=k-self.dts
         t_node = node[0]

         if node[1]==1:
             self.dis=0
             Solution.dfs(self,t_node.left,dis-1)
         else:
             Solution.dfs(self, t_node.right, dis - 1)

         self.get_res(self,target,k,t_node)








