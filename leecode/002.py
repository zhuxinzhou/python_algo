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
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class List(object):
    def __init__(self, first=None):
        self.first = first
    def insert_to_head(self,val):
        node=ListNode(val)
        node.next=self.first
        self.first=node
    def get(self):
        return self.first

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type lx1: ListNode
        :type lx2: ListNode
        :rtype: ListNode
        """
        lx1=[]
        lx2=[]
        while l1.next:
            lx1.append(l1.val)
            l1=l1.next
        lx1.append(l1.val)
        while l2.next:
            lx2.append(l2.val)
            l2 = l2.next
        lx2.append(l2.val)
        length1=len(lx1)
        length2=len(lx2)

        nums1 = 0
        for i in range(length1):
            key1 = lx1[length1 - 1 - i]
            beishu = 1

            for t in range(length1 - i - 1):
                beishu = 10 * beishu
            print(key1 * beishu)
            nums1 = key1 * beishu + nums1

        nums2 = 0
        for i in range(length2):
            key2 = lx2[length2 - 1 - i]
            beishu = 1

            for t in range(length2 - i - 1):
                beishu = 10 * beishu
            print(key2 * beishu)
            nums2 = key2 * beishu + nums2

        res=nums1+nums2
        res=str(res)
        leres=len(res)
        print('here',res)
        result=[]
        linklist=List()
        for i in range(leres):
            linklist.insert_to_head(int(res[i]))





        return linklist.get()


linklist = List()
l1=[2,3,4]
for i in range(len(l1)):
    linklist.insert_to_head(l1[i])
lx1=[]
l1=linklist.get()
while l1.next:
      lx1.append(l1.val)
      l1=l1.next
lx1.append(l1.val)
print(lx1)
l2=l1
so=Solution()
l1=so.addTwoNumbers(l1,l2)
lx1=[]
while l1.next:
      lx1.append(l1.val)
      l1=l1.next

print(lx1)