'''
-*- coding: utf-8 -*-
@Author  : zoeyzhu
@Time    : 2021/7/22 11:01 下午
@Software: PyCharm
@File    : 003.py
@function:
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length=len(s)
        max=0
        max_list=[]
        flag=0
        tem = []
        j=0
        for i in range(length):
            tem = []
            for j in range(i,length):
                if s[j] in tem:
                    flag=1
                    if max<len(tem):
                        max=len(tem)
                    break
                else:
                    flag=2
                    tem.append(s[j])
            if flag == 2:
                j = j - 1
                if max < len(tem):
                    max = len(tem)
        if flag==0:
            max=len(s)

        return max

n=Solution()
print(n.lengthOfLongestSubstring("aab"))