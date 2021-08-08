'''
-*- coding: utf-8 -*-
@Author  : zoeyzhu
@Time    : 2021/8/6 8:05 下午
@Software: PyCharm
@File    : 847.py
@function:
存在一个由 n 个节点组成的无向连通图，图中的节点按从 0 到 n - 1 编号。

给你一个数组 graph 表示这个图。其中，graph[i] 是一个列表，由所有与节点 i 直接相连的节点组成。

返回能够访问所有节点的最短路径的长度。你可以在任一节点开始和停止，也可以多次重访节点，并且可以重用边。

 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shortest-path-visiting-all-nodes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List

class Solution:
    def __init__(self):
        self.minx=9999
        self.havesee=[]
        self.color=[]
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        length=len(graph)
        have_see=[]
        def dfs(i,last):
            last=last+1
            print('sec',i,self.have_see)
            if i not in self.have_see:
                self.have_see.append(i)
            if len(self.have_see)==length:
                print('k', self.have_see)
                if last<self.minx:
                    self.minx=last
                return
            # print('dfs',i)
            for item in graph[i]:
                if i==2:
                    print('dn',self.color,i,item)
                # print('ds', self.color, i, item)

                if [i,item] in self.color:
                    continue

                if graph[item][0]==i:
                    return
                self.color.append([i,item])
                dfs(item,last)



        for item in range(length):
            self.color = []
            self.have_see = []
            print('first',item)
            # print(item)
            dfs(item,0)
        print((self.minx))
        return (self.minx)


s=Solution()
graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
s.shortestPathLength(graph=graph)