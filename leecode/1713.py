'''
-*- coding: utf-8 -*-
@Author  : zoeyzhu
@Time    : 2021/7/26 10:49 下午
@Software: PyCharm
@File    : 1713.py
@function:
给你一个数组 target ，包含若干 互不相同 的整数，以及另一个整数数组 arr ，arr 可能 包含重复元素。

每一次操作中，你可以在 arr 的任意位置插入任一整数。比方说，如果 arr = [1,4,1,2] ，那么你可以在中间添加 3 得到 [1,4,3,1,2] 。你可以在数组最开始或最后面添加整数。

请你返回 最少 操作次数，使得 target 成为 arr 的一个子序列。

一个数组的 子序列 指的是删除原数组的某些元素（可能一个元素都不删除），同时不改变其余元素的相对顺序得到的数组。比方说，[2,7,4] 是 [4,2,3,7,2,1,4] 的子序列（加粗元素），但 [2,4,2] 不是子序列。

 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-operations-to-make-a-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List

def get_psu(list,pos,lenx):
    # print(list)
    # print(pos)

    for i in range(len(list)):
        if list[i]>pos-lenx:
            return list[i]
    return None
class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        a=dict()
        b=dict()
        x=dict()
        for i in range(len(arr)):
            x[arr[i]]=i
            if arr[i] in a.keys():
               a[arr[i]].append(i)
            else:
                a_list=[]
                a_list.append(i)
                a[arr[i]]=a_list
        # print(a)
        for i in range(len(target)):
            b[target[i]] = i  # 记录位置
        #判断target元素在arr中的位置,并进行记录当前的元素，若无
        pos=0
        lenx=0
        for item in target:
            if item in x.keys():
                tem_pos=a[item]
                tem_posr=get_psu(tem_pos,pos,lenx)
                # print(lenx, item,tem_posr,pos)
                if tem_posr:
                    pos=tem_posr
                else:
                    pos=pos+1
                    lenx=lenx+1
            else:
                # print(lenx, item)
                pos = pos + 1
                lenx = lenx + 1
        print(lenx)
        return lenx

s=Solution()
target=[16,7,20,11,15,13,10,14,6,8]
arr=[11,14,15,7,5,5,6,10,11,6]
s.minOperations(target,arr)

# print(len(target))