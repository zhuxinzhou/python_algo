'''
-*- coding: utf-8 -*-
@Author  : zoeyzhu
@Time    : 2021/7/19 10:58 下午
@Software: PyCharm
@File    : 002.py
@function:
 两数相加
 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# class Solution(object):
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         p1=l1
#         p2=l2
#         jinwei=0
#         head=None
#         while p1 or p2:
#             #获取两个的值
#             key1=p1.val if p1 else 0
#             key2=p2.val if p2 else 0
#             sum=0
#             if jinwei==0:
#                 sum=key1+key2
#             else:
#                 sum=key1+key2+jinwei
#                 jinwei=0
#             new_node_val=0
#             if sum>=10:
#                 #超出了
#                 new_node_val=sum-10
#                 jinwei=1
#             else:
#                 new_node_val=sum
#             new_node=ListNode(new_node_val,None)
#             if head==None:
#                 head=new_node
#             else:
#                 p=head
#                 while p.next:
#                     p=p.next
#                 p.next=new_node
#             p1=p1.next if p1 else None
#             p2=p2.next if p2 else None
#
#         if jinwei:
#             new_node=ListNode(1)
#             p = head
#             while p.next:
#                 p = p.next
#             p.next = new_node
#
#         return head


#滑动窗口解法
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left=0
        right=0
        max=0
        tem={}
        length=len(s)
        for i in s:
            tem[i]=0
        le=0
        flag=0
        while left<=right and right<length:
            if tem[s[right]]==0:
                tem[s[right]]=1
                right=right+1
                le=le+1
            else:
                if le>max:
                    max=le
                    flag=1
                le=le-1
                tem[s[left]]=0
                left=left+1
        if le > max:
            max = le
            flag = 1
        if flag==0:
            max=length
        return max

s=Solution()
s.lengthOfLongestSubstring("aab")
