'''
-*- coding: utf-8 -*-
@Author  : zoeyzhu
@Time    : 2021/8/3 10:42 下午
@Software: PyCharm
@File    : binary_search_tree.py
@function:
搜索数的相应操作
'''

class Treenode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        self.parent=None
class BinarySearchTree:
    def __init__(self,val_list=[]):
        self.root=None
        for n in val_list:
            self.insert(n)
    def insert(self,data):
        if self.root is None:
            self.root=Treenode(data)
        else:
            n=self.root
            while n:
                p=n
                if data<n.val:
                    n=n.left
                else:
                    n=n.right
            new_node= Treenode(data)
            new_node.parent=p
            if data<p.val:
                p.left=new_node
            else:
                p.right=new_node
            return True

    def search(self,data):
        n=self.root
        ret = []

        n = self.root
        while n:
            if data < n.val:
                n = n.left
            else:
                if data == n.val:
                    ret.append(n)
                n = n.right

        return ret

    def delete(self,data):

        del_list=self.search(data)
        for n in del_list:
            if n.parent is None and n != self.root:
                continue
            else:
                self._del(n)
    def _del(self,node):
        '''
        删除
        所删除的节点N存在以下情况：
        1. 没有子节点：直接删除N的父节点指针
        2. 有一个子节点：将N父节点指针指向N的子节点
        3. 有两个子节点：找到右子树的最小节点M，将值赋给N，然后删除M
        :param node:
        :return:
        '''
        # 没有子节点：直接删除N的父节点指针
        if node.left is None and node.right is None:
            if node==self.root:
                self.root=None
            else:
                if node.val<node.partent.val:
                    node.parent.left=None
                else:
                    node.parent.right=None
                node.parent=None
        # 有一个子节点：将N父节点指针指向N的子节点
        elif node.left is None and node.right is not None:
            if node ==self.root:
                self.root=node.right
                self.root.parent=None
                node.right=None
            else:
                #根据node的值来分
                if node.val<node.parent.val:
                    node.parent.left=node.right
                else:
                    node.parent.right = node.left
                node.left.parent = node.parent
                node.parent = None
                node.left = None
            # 3
        else:
            min_node = node.right
                # 找到右子树的最小值节点
            if min_node.left:
                min_node = min_node.left

            if node.val != min_node.val:
                node.val = min_node.val
                self._del(min_node)
                # 右子树的最小值节点与被删除节点的值相等，再次删除原节点
            else:
                self._del(min_node)
                self._del(node)

    def get_min(self):
        """
        返回最小值节点
        :return:
        """
        if self.root is None:
            return None

        n = self.root
        while n.left:
            n = n.left
        return n.val

    def get_max(self):
        """
        返回最大值节点
        :return:
        """
        if self.root is None:
            return None

        n = self.root
        while n.right:
            n = n.right
        return n.val
