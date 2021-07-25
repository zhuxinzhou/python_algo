'''
-*- coding: utf-8 -*-
@Author  : zoeyzhu
@Time    : 2021/7/22 10:03 下午
@Software: PyCharm
@File    : 138.py
@function:
给你一个长度为 n 的链表，每个节点包含一个额外增加的随机指针 random ，该指针可以指向链表中的任何节点或空节点。

构造这个链表的 深拷贝。 深拷贝应该正好由 n 个 全新 节点组成，其中每个新节点的值都设为其对应的原节点的值。新节点的 next 指针和 random 指针也都应指向复制链表中的新节点，并使原链表和复制链表中的这些指针能够表示相同的链表状态。复制链表中的指针都不应指向原链表中的节点 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/copy-list-with-random-pointer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        p=head
        d=dict()
        while p:
            new_node=Node(p.val,None,None)
            d[p]=new_node
            p=p.next
        p=head
        while p:
            if p.next:
                d[p].next=d[p.next]
            if p.random:
                d[p].random=d[p.random]
            p=p.next
        return d[head]

