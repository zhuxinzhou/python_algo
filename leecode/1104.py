'''
-*- coding: utf-8 -*-
@Author  : zoeyzhu
@Time    : 2021/7/29 10:30 下午
@Software: PyCharm
@File    : 1104.py
@function:
在一棵无限的二叉树上，每个节点都有两个子节点，树中的节点 逐行 依次按 “之” 字形进行标记。

如下图所示，在奇数行（即，第一行、第三行、第五行……）中，按从左到右的顺序进行标记；

而偶数行（即，第二行、第四行、第六行……）中，按从右到左的顺序进行标记。

给你树上某一个节点的标号 label，请你返回从根节点到该标号为 label 节点的路径，该路径是由途经的节点标号所组成的。

'''
from typing import List
def get_road(list,label):
    list.reverse()
    print('yyy',list)
    i_list=list[0]
    res=[]
    # res.append(label)
    i_d = i_list.index(label)
    # for i in range(len(t_list)):
    for item in list:
        # print(item[i_d])
        res.append(item[i_d])
        i_d=int(i_d/2)
    return res


class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        j=1
        now=1
        if label==1:
            return [1]
        mul=1
        res=[]
        a=[1]
        res.append(a)
        while label>=now :
            j=2**mul
            now=2**(mul+1)
            tem = []
            for k in range(j,now):
                tem.append(k)
            if mul%2==1:
                tem.reverse()
            res.append(tem)
            mul=mul+1
        rt=get_road(res,label)
        rt.reverse()
        return rt





s=Solution()
print('key',s.pathInZigZagTree(14))