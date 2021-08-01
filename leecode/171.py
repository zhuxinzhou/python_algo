'''
-*- coding: utf-8 -*-
@Author  : zoeyzhu
@Time    : 2021/7/30 8:52 下午
@Software: PyCharm
@File    : 171.py
@function:
给你一个字符串 columnTitle ，表示 Excel 表格中的列名称。返回该列名称对应的列序号。

例如，

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...


示例 1:
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/excel-sheet-column-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
a=dict()
a={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,\
   'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,\
   'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,\
   'Z':26
   }
print(a)
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res_=[]
        for item in columnTitle:
            res_.append(item)
        # print(res_)
        sum=0
        for i in range(len(res_)):
            k=len(res_)-i-1
            sum=sum+a[res_[k]]*26**i
        print(sum)
        return sum
s=Solution()
s.titleToNumber('Z')