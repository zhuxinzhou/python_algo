'''
-*- coding: utf-8 -*-
@Author  : zoeyzhu
@Time    : 2021/8/3 8:11 下午
@Software: PyCharm
@File    : 581.py.py
@function:
给你一个整数数组 nums ，你需要找出一个 连续子数组 ，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。

请你找出符合题意的 最短 子数组，并输出它的长度。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:

        def compare(nums):
            left=-1
            tlist = []

            for item in nums:
                tlist.append(item)
            tlist.sort()
            print(tlist)
            print(nums)
            right=len(nums)
            for i in range(len(tlist)):
                if tlist[i]==nums[i]:
                    left=left+1
                else:
                    break
            for i in range(len(tlist)):
                key=len(tlist)-i-1
                if tlist[key] == nums[key]:
                    right = right -1
                else:
                    break
            print(right)
            print(left)
            return right-left-1
        key=compare(nums)
        if key<=0 or key>=len(nums):
            return 0
        else:
            return key

nums = [1,2,3,4]

s=Solution()
s.findUnsortedSubarray(nums)