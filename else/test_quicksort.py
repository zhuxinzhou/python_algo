'''
-*- coding: utf-8 -*-
@Author  : zoeyzhu
@Time    : 2021/7/22 9:37 下午
@Software: PyCharm
@File    : test_quicksort.py
@function:
实现快速排序
'''
import random
from typing import List

def quicksort(a:List[int]):
   low=0
   high=len(a)-1
   quick_sort_between(a,low,high)
   print(a)

def quick_sort_between(a:List[int],low:int,high:int):
    if low<high:
        k=random.randint(low,high)
        a[low],a[k]=a[k],a[low]
        m=_partition(a,low,high)
        quick_sort_between(a,low,m-1)
        quick_sort_between(a,m+1,high)

def _partition(a:List[int],low:int,high:int):
    pivot,j=a[low],low
    for i in range(low+1,high+1):
        if a[i]<pivot:
            #交换位位置
            j+=1
            a[j], a[i] = a[i], a[j]  # swap
    a[low], a[j] = a[j], a[low]#统一把ak和a[j]互换
    return j#最后小于的位置

a=[1,3,2,4,6,7,12,3,4,88,12]
quicksort(a)