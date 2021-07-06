'''
-*- coding: utf-8 -*-
@Author  : zoeyzhu
@Time    : 2021/7/4 11:29 下午
@Software: PyCharm
@File    : singlyLinkList.py
@function:
实现单链表的相关操作，初始化，取中间值，判断是否有环
'''
class Node(object):
    def __init__(self,data,next_node=None):
        self.__data=data
        self.__next=next_node
    '''
    @property介绍
    Python内置的@property装饰器就是负责把一个方法变成属性调用的：
    时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值
    '''
    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self,data):
        self.__data=data
    @property
    def next_node(self):
        return self.__next
    @next_node.setter
    def next_node(self,next_node):
        self.__next=next_node

class SinglyLinkedList(object):
    def __init__(self):
        #单链表初始化操作，初始化首节点
        self.__head= None
    def find_by_value(self,value):
        #根据数据链表
        node =self.__head
        while (node is not None) and (node.data!=value):
            node=node.next_node
        return node
    def find_by_index(self,index):
        node =self.__head
        pos=0
        while (node is not None) and (pos!=index):
            node=node.next_node
            pos=pos+1
        return node
    def insert_to_head(self,value):
        #在首节点插入，初始化一个node，node的下一个节点时首节点
        #然后把单链表的首节点
        node=Node(value)
        node.next_node=self.__head
        self.__head=node
    def insert_after(self,node,value):
        #在链表的某个指定Node节点之前插入一个存储value数据的Node节点.
        if (node is None) or (self.__head is None):
            return

        new_node=Node(value)
        new_node.next_node=node.next_node
        node.next_node=new_node
    def insert_before(self,node,value):
        '''
        在一个节点前插，比较麻烦
        首先要找到这个节点的前置节点
        在前置节点前插的前
        :param node:
        :param value:
        :return:
        '''
        if (node is None) or (self.__head==None):
            return
        if node == self.__head:  # 在首节点则直接插入
            self.insert_to_head(value)
            return
        new_node=Node(value)
        pro=self.__head
        not_found=False
        while pro.next_node!= node:#寻找前面一个节点
            if pro.next_node is None:
                not_found=True
                return
            else:
                pro=pro.next_node

        if not not_found:
            pro.next_node=new_node
            new_node.next_node=node
    def delete_by_node(self,node):
        if self.__head is None:
            return
        if node ==self.__head:
            self.__head==node.next_node
            return
        pro = self.__head
        not_found = False  # 如果在整个链表中都没有找到指定删除的Node节点，则该标记量设置为True
        while pro.next_node != node:
            if pro.next_node is None:  # 如果已经到链表的最后一个节点，则表明该链表中没有找到指定删除的Node节点
                not_found = True
                break
            else:
                pro = pro.next_node
        if not not_found:
            pro.next_node = node.next_node
    def delete_by_value(self,value):
        #如果空链表，不操作
        if(self.__head is None):
            return
        node=self.__head
        have_find=True
        while((node.data!=value)):
            if node.next_node==None:
                have_find=False
                break
            else:
                pro=node
                node=node.next_node
        if have_find:
            pro.next_node=node.next_node
    def delete_last_n_node(self,n):
        '''
          设置快、慢两个指针，快指针先行，慢指针不动；当快指针跨了N步以后，快、慢指针同时往链表尾部移动，
            当快指针到达链表尾部的时候，慢指针所指向的就是链表的倒数第N个节点
        :param n:
        :return:
        '''
        fast=self.__head
        slow=self.__head
        step=0
        while step<=n:
            fast=fast.next_node
            step=step+1
        while fast.next_node is not None:
            tem=slow
            fast=fast.next_node
            slow=slow.next_node
        tem.next_node=slow.next_node
    def find_mid_node(self):
        '''
        设置快慢两个节点，快节点一次走两遍，慢节点走一步，
        :return:
        '''
        if self.__head is None:
            return
        fast=self.__head
        slow=self.__head
        while(fast.next_node!=None):
            slow=slow.next_node
            fast=fast.next_node
            if fast is None:
                break
            else:
                fast=fast.next_node
            if fast is None:
                break
        return slow
    def create_node(self,value):
        return Node(value)
    def print_all(self):
        pos=self.__head
        if pos is None:
            print('当前链表没有数据')
            return
        while pos.next_node is not None:
            print(str(pos.data)+"-->",end="")
            #end参数可以用来不换行
            pos=pos.next_node
        print(str(pos.data))







    def has_ring(self):
        """检查链表中是否有环.
        主体思想：
            设置快、慢两种指针，快指针每次跨两步，慢指针每次跨一步，如果快指针没有与慢指针相遇而是顺利到达链表尾部
            说明没有环；否则，存在环
        返回:
            True:有环
            False:没有环
        """
        fast = self.__head
        slow = self.__head

        while (fast.next_node is not None) and (fast is not None):
            fast = fast.next_node
            slow = slow.next_node
            if fast.next_node==None:
                return False
            fast=fast.next_node
            print(fast.data,slow.data)
            if fast == slow:
                return True

        return False

    def reversed_self(self):
        if self.__head is None or self.__head.next_node is None:  # 如果链表为空，或者链表只有一个节点
            return

        node = self.__head
        new_list = SinglyLinkedList()
        while node is not None:
            new_list.insert_to_head(node.data)
            node = node.next_node
        return new_list
    def make_cicle_list(self):
        #制作循环链表
        if self.__head==None:
            return
        node=self.__head
        while(node.next_node!=None):
            node=node.next_node
            if (node.next_node==None):
                node.next_node=self.__head
                return





if __name__ == "__main__":
    slist=SinglyLinkedList()
    slist.insert_to_head(5)
    slist.insert_to_head(4)
    slist.insert_to_head(3)
    slist.insert_to_head(2)
    slist.insert_to_head(1)
    slist.insert_to_head(5)
    # slist.make_cicle_list()
    mid=slist.find_mid_node()
    # slist.delete_by_value(4)
    # slist.delete_by_node(mid)
    print(mid.data)
    # print(slist.find_mid_node())
    slist.print_all()
    relist=slist.reversed_self()
    relist.print_all()
    slist.print_all()
