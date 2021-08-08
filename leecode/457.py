'''
-*- coding: utf-8 -*-
@Author  : zoeyzhu
@Time    : 2021/8/7 10:08 下午
@Software: PyCharm
@File    : 457.py
@function:
'''
from typing import List

class Solution:
    def circularArrayLoop(self,nums:List[int]) ->bool:
        n=len(nums)
        def next(cur:int) ->int:
            return (cur+nums[cur])%n

        for i,num in enumerate(nums):
            if num==0:
                continue
            slow,fast=i,next(i)
            while nums[slow] * nums[fast] > 0 and nums[slow] * nums[next(fast)] > 0:
                if slow == fast:
                    if slow == next(slow):
                        break
                    return True
                slow = next(slow)
                fast = next(next(fast))
            add = i
            while nums[add] * nums[next(add)] > 0:
                tmp = add
                add = next(add)
                nums[tmp] = 0
        return False
