'''
-*- coding: utf-8 -*-
@Author  : zoeyzhu
@Time    : 2021/8/9 3:07 下午
@Software: PyCharm
@File    : bfs&dfs.py
@function:
深搜和广搜
'''
from collections import deque
class Graph:
    def __init__(self,num_vertices):
        self.num_vertices = num_vertices
        self._adj=[[] for _ in range(num_vertices)]
    def add_edge(self,s:int,t:int) ->None:
        self._adj[s].append(t)
        self._adj[t].append(s)
    def _generate_path(self,s:int,t:int,prev):
        if prev[t] or s!=t:
            yield from self._generate_path(s, prev[t], prev)
        yield str(t)
    def bfs(self,s:int,t:int):
        if s==t:return
        visited=[False]*self.num_vertices
        visited[s]=True
        q=deque()
        q.append(s)
        prev = [None] * self._num_vertices
        while q:
            v=q.popleft()
            for neighbour in self._adj[v]:
                if not visited[neighbour]:
                    prev[neighbour]=v
                    if neighbour == t:
                        print("->".join(self._generate_path(s, t, prev)))
                        return
                    visited[neighbour]=True
                    q.append(neighbour)
    def dfs(self,s:int,t:int):
        found=False
        visited=[False]*self.num_vertices
        prev=[None]*self.num_vertices
        def _dfs(from_vertex:int) ->None:
            nonlocal found
            if found: return
            visited[from_vertex] = True
            if from_vertex == t:
                found = True
                return
            for neighbour in self._adj[from_vertex]:

                if not visited[neighbour]:
                    prev[neighbour] = from_vertex
                    _dfs(neighbour)

            _dfs(s)
            print("->".join(self._generate_path(s, t, prev)))
