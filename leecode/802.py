'''
-*- coding: utf-8 -*-
@Author  : zoeyzhu
@Time    : 2021/8/5 9:56 下午
@Software: PyCharm
@File    : 802.py
@function:
在有向图中，以某个节点为起始节点，从该点出发，每一步沿着图中的一条有向边行走。如果到达的节点是终点（即它没有连出的有向边），则停止。

对于一个起始节点，如果从该节点出发，无论每一步选择沿哪条有向边行走，最后必然在有限步内到达终点，则将该起始节点称作是 安全 的。

返回一个由图中所有安全的起始节点组成的数组作为答案。答案数组中的元素应当按 升序 排列。

该有向图有 n 个节点，按 0 到 n - 1 编号，其中 n 是 graph 的节点数。图以下述形式给出：graph[i] 是编号 j 节点的一个列表，满足 (i, j) 是图的一条有向边。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-eventual-safe-states
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
class node:
    def __init__(self,val):
        self.val=val
        self.list=[]
        self.data=[]
        self.flag=0
class Solution:
    def __init__(self):
        self._res=[]
        self.have_see={}
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        length=len(graph)
        color=[0]*length
        print(color)
        def safe(k):
            if color[k]>1:
                return color[k]==2
 
            for t in graph[k]:
                if not safe(t):
                    return False
            color[k]=2
            return True
        print( [ i for i in range(length) if safe(i)])
        return [ i for i in range(length) if safe(i)]


s=Solution()
graph = [[],[0,2,3,4],[3],[4],[]]
s.eventualSafeNodes(graph)