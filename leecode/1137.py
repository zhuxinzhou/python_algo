'''
-*- coding: utf-8 -*-
@Author  : zoeyzhu
@Time    : 2021/8/8 9:34 下午
@Software: PyCharm
@File    : 1137.py
@function:
泰波那契序列 Tn 定义如下： 

T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2

给你整数 n，请返回第 n 个泰波那契数 Tn 的值。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/n-th-tribonacci-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
class Solution:
    def __init__(self):
        self.a=dict()
    def tribonacci(self, n: int) -> int:
        # print(n)


        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        if n in self.a.keys():
            return self.a[n]
        data=self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
        self.a[n]=data
        return data



s=Solution()
print(s.tribonacci(25))