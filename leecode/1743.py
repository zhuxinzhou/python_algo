'''
-*- coding: utf-8 -*-
@Author  : zoeyzhu
@Time    : 2021/7/25 10:26 下午
@Software: PyCharm
@File    : 1743.py
@function:
存在一个由 n 个不同元素组成的整数数组 nums ，但你已经记不清具体内容。好在你还记得 nums 中的每一对相邻元素。

给你一个二维整数数组 adjacentPairs ，大小为 n - 1 ，其中每个 adjacentPairs[i] = [ui, vi] 表示元素 ui 和 vi 在 nums 中相邻。

题目数据保证所有由元素 nums[i] 和 nums[i+1] 组成的相邻元素对都存在于 adjacentPairs 中，存在形式可能是 [nums[i], nums[i+1]] ，也可能是 [nums[i+1], nums[i]] 。这些相邻元素对可以 按任意顺序 出现。

返回 原始数组 nums 。如果存在多种解答，返回 其中任意一个 即可。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/restore-the-array-from-adjacent-pairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
class node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
    def setnode(self,n):
        if self.left==None:
            self.left=n
        elif self.right==None:
            self.right=n
        else:
            print('wrong')
    def is_sigle(self):
        if self.left==None:
            return True
        if self.right==None:
            return True
        return False
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        a=dict()
        for item in adjacentPairs:
              key1=item[0]
              key2=item[1]
              if key1 in a.keys():
                  n1=a[key1]
              else:
                  n1 = node(key1)
                  a[key1]=n1
              if key2 in a.keys():
                  n2 = a[key2]
              else:
                  n2= node(key2)
                  a[key2] = n2

              n1.setnode(n2)
              n2.setnode(n1)
        start=None
        result =[]
        d=dict()
        for item in a.keys():
            n=a[item]
            if n.is_sigle():
                start=n
                break
        while 1:
            key=start.val
            if key not in d.keys():
                result.append(key)
                d[key]=1
            n1=start.left
            n2=start.right
            if n1 and n1.val not in d.keys():
                start=n1
            if n2 and n2.val not in d.keys():
                start = n2

            if not n1 and n2.val in d.keys():
                break
            if not n2 and n1.val in d.keys():
                break
        # print(result)
        return result

s=Solution()
list=[[4,-2],[1,4],[-3,1]]
s.restoreArray(list)
