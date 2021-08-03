'''
-*- coding: utf-8 -*-
@Author  : zoeyzhu
@Time    : 2021/8/2 9:38 下午
@Software: PyCharm
@File    : 743.py
@function:
有 n 个网络节点，标记为 1 到 n。

给你一个列表 times，表示信号经过 有向 边的传递时间。 times[i] = (ui, vi, wi)，其中 ui 是源节点，vi 是目标节点， wi 是一个信号从源节点传递到目标节点的时间。

现在，从某个节点 K 发出一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回 -1 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/network-delay-time
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
import sys  # 导入sys模块
sys.setrecursionlimit(30000)
class Solution:
    def __init__(self):
        self.dis=0
        self.a=dict()
        self.arrive=[]
        self.nodenum=0
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #n是节点，k是开始
        b=dict()
        self.arrive = [float('inf')] * (n +1)
        for item in times:
           if item[0] in b.keys():
               b[item[0]][item[1]]=item[2]
           else:
               b[item[0]]={}

               b[item[0]][item[1]] = item[2]
        Solution.dfs(self,b,k,0)
        ans=float('inf')
        for time in self.arrive:
            if time==float('inf'):
                return -1
            if ans<time:
                ans=time
        return ans

    def dfs(self,b: dict, k,time):
        if self.arrive[k]<=time or k not in b.keys():
            return
        self.arrive[k]=time
        for item in b[k].keys():
            Solution.dfs(self,b,item,time + b[k][item])
times = [[1,2,1],[2,3,2],[1,3,2]]
n = 4
k = 2
s=Solution()
print('res',s.networkDelayTime(times,n,k))
# print(b[1][1])
g = [[float('inf')] * n for _ in range(n)]
print(g)