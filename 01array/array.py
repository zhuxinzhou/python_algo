'''
-*- coding: utf-8 -*-
@Author  : zoeyzhu
@Time    : 2021/7/4 10:28 下午
@Software: PyCharm
@File    : array.py
@function:
python 实现数组代码，
数组是一种使用连续空间，存储相同数据类型的数据结构
从0开始
'''
class MyArray:
    def __init__(self,capacity:int):#python 类初始化
        self._data=[]#list存储
        self._capacity=capacity#容量

    def __getitem__(self,position:int) ->object:
        return self._data[position]
    def __setitem__(self,index:int,value:object):
        self._data[index] =value
    def __len__(self)->int:
        return len(self._data)
    def __iter__(self)->int:
        for item in self._data:
            yield item #yield就是 return 返回一个值，并且记住这个返回的位置，下次迭代就从这个位置后开始。
    def find(self,index:int)->object:
        try:
            return self._data[index]
        except IndexError:
            return None
    def delete(self, index:int):
        try:
            self._data.pop(index)
            return True
        except IndexError:
            return False
    def insert(self,index:int,value:int) ->bool:
        if len(self)>=self._capacity:
            return False
        else:
            return self._data.insert(index,value)
    def print_all(self):
        for item in self:
            print(item)
def test_myarray():
    array= MyArray(5)
    array.insert(0,3)
    array.insert(0,4)
    array.insert(1, 5)
    array.insert(3, 9)
    array.insert(3, 10)
    array.__iter__()
    '''
     assert True     # 条件为 true 正常执行
>>> assert False    # 条件为 false 触发异常
    '''
    assert array.insert(0, 100) is False
    assert len(array) == 5
    assert array.find(1) == 5
    assert array.delete(4) is True
    array.print_all()
if __name__ == "__main__":
    test_myarray()
print('hello')