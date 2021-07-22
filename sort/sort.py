'''
-*- coding: utf-8 -*-
@Author  : zoeyzhu
@Time    : 2021/7/17 2:30 下午
@Software: PyCharm
@File    : sort.py
@function:
排序算法，空间复杂度为o(1)的算法：冒泡排序，插入排序，选择排序，空间复杂度为on方
'''
from typing import List
#冒泡排序
import random
def bubble_sort(a: List[int]):
    length=len(a)
    if length<=1:
        return
    for i in range(length):
        for j in range(length-i-1):
            if(a[j]>a[j+1]):
                a[j],a[j+1]=a[j+1],a[j]
    print(a)

#插入排序
def insertion_sort(a:List[int]):
    length=len(a)
    if length<=1:
        return

    for i in range(1,length):
        value=a[i]
        #当前值的前一位
        j=i-1
        #定位到当前位置，确保j前有序
        while j>=0 and a[j]>value:
            a[j+1]=a[j]
            j-=1
        a[j+1]=value
    print(a)

#选择排序
def selection_sort(a:List[int]):
    length=len(a)
    #排序区和为排序区，把未排序区最小的插到排序去
    for i in range(length):
        key = i
        min=a[i]
        minindex=i
        for j in range(i+1,length):
            if a[j]<min:
                min=a[j]
                minindex=j
        #交换数据
        tem=a[i]
        a[i]=min
        a[minindex]=tem

    print(a)

#归并排序
def merge_sort(a:List[int]):
    _merge_sort_between(a,0,len(a)-1)
    print(a)
def _merge_sort_between(a: List[int], low: int, high: int):
    if low < high:
        mid = low + (high - low) // 2
        _merge_sort_between(a, low, mid)
        _merge_sort_between(a, mid + 1, high)
        _merge(a, low, mid, high)


def _merge(a: List[int], low: int, mid: int, high: int):
    i, j = low, mid + 1
    tmp = []
    '''
    申请一个临时数组 tmp，大小与 A[p…r] 相同。
    我们用两个游标 i 和 j，分别指向 A[p…q] 和 A[q+1…r] 的第一个元素。
    比较这两个元素 A[i] 和 A[j]，
    如果 A[i]<=A[j]，我们就把 A[i] 放入到临时数组 tmp，
    并且 i 后移一位，否则将 A[j] 放入到数组 tmp，j 后移一位。
    '''
    while i <= mid and j <= high:
        if a[i] <= a[j]:
            tmp.append(a[i])
            i += 1
        else:
            tmp.append(a[j])
            j += 1
    start = i if i <= mid else j
    end = mid if i <= mid else high
    #extend() 函数用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）。
    #当while结束后，需要将后续当内容留下
    tmp.extend(a[start:end + 1])
    a[low:high + 1] = tmp

#快速排序
def quick_sort(a:List[int]):
    _quick_sort_between(a,0,len(a)-1)
def _quick_sort_between(a:List[int],low:int,high:int):
    if low<high:
        k=random.randint(low,high)
        a[low],a[k]=a[k],a[low]
        m=_partition(a,low,high)#a[m]是最后的一个位置
        _quick_sort_between(a,low,m-1)
        _quick_sort_between(a,m+1,high)
def _partition(a:List[int],low:int,high:int):
    pivot, j = a[low], low#本来应该是k，把k放到首位
    #小于k的发在k后面
    for i in range(low + 1, high + 1):
        if a[i] <= pivot:
            j += 1
            a[j], a[i] = a[i], a[j]  # swap
    a[low], a[j] = a[j], a[low]#统一把ak和a[j]互换
    return j



a=[67,2,3,1,4,6,23,4,2,87,12]

insertion_sort(a)
selection_sort(a)
merge_sort(a)

