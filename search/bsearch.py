'''
-*- coding: utf-8 -*-
@Author  : zoeyzhu
@Time    : 2021/7/25 11:10 下午
@Software: PyCharm
@File    : bsearch.py
@function:
实现简单二分查找，分别以递归和非递归方式实现
'''
from typing import List
#循环实现
class bsearch():
    def __init__(self):
        pass
    def bssearchbycycle(self,nums:List[int],target:int) ->int:
        low,high = 0,len(nums)-1
        while low<=high:
            mid = low+(high-low)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<=target:
                low=mid+1
            else:
                high=mid-1

        return -1

#递归实现
def bssearchBydg(nums: List[int], target: int) -> int:
    return bssearchBydg(nums, 0, len(nums)-1, target)
def bsearch_internally(nums: List[int], low: int, high: int, target: int) -> int:
    if low>high:
        return -1
    mid = low+(high-low)>>2
    if nums[mid] ==target:
        return mid
    elif nums[mid]<target:
        bsearch_internally(nums,mid+1,high,target)
    else:
        bsearch_internally(nums,low,mid-1,target)

#当有重复的数据时
#找最左边第一个相同的数据
'''
a[mid] 的前一个元素 a[mid-1] 不等于 value，那也说明 a[mid] 就是我们要找的第一个值等于给定值的元素。
'''
#high左移动
def bsearch_left(nums:List[int],target:int) -> int:
    low,high=0,len(nums)-1
    while low<=high:
        mid=low+(high-low)//2
        if nums[mid]<target:
            low=mid+1
        else:
            high=mid-1
    if high!=0 and nums[high]==target:
        return  high
    else:
        return -1
#等于情况high右移
def bsearch_right(nums: List[int], target: int) -> int:
    """Binary search of the index of the last element
    equal to a given target in the ascending sorted array.
    If not found, return -1.
    """
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] <= target:
            low = mid + 1
        else:
            high = mid - 1
    if high >= 0 and nums[high] == target:
        return high
    else:
        return -1



def bsearch_left_not_less(nums: List[int], target: int) -> int:
    """Binary search of the index of the first element
    not less than a given target in the ascending sorted array.
    If not found, return -1.
    """
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    if low < len(nums) and nums[low] >= target:
        return low
    else:
        return -1

def bsearch_right_not_greater(nums: List[int], target: int) -> int:
    """Binary search of the index of the last element
    not greater than a given target in the ascending sorted array.
    If not found, return -1.
    """
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] <= target:
            low = mid + 1
        else:
            high = mid - 1
    if high >= 0 and nums[high] <= target:
        return high
    else:
        return -1
