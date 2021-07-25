'''
-*- coding: utf-8 -*-
@Author  : zoeyzhu
@Time    : 2021/7/24 9:20 下午
@Software: PyCharm
@File    : 1736.py
@function:
给你一个字符串 time ，格式为 hh:mm（小时：分钟），其中某几位数字被隐藏（用 ? 表示）。

有效的时间为 00:00 到 23:59 之间的所有时间，包括 00:00 和 23:59 。

替换 time 中隐藏的数字，返回你可以得到的最晚有效时间。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/latest-time-by-replacing-hidden-digits
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def maximumTime(self, time: str) -> str:
        '''
        开始讨论：
        第一位：2，
        第二位:1，[0,1]:9,2:4
        ；
        第二部分:
        第一位：5，
        第二位：9
        :param time:
        :return:
        '''
        time_list=[]
        tem=time
        time_list=tem.split(':')
        t1=time_list[0]
        t2=time_list[1]
        s1=t1[0]
        s2=t1[1]
        s3=t2[0]
        s4=t2[1]
        if s1=='?':
            if (s3=='0' and s4 =='0'and s2<'4') or s2<'4' or s2=='?':
                s1='2'
            else:
                s1='1'
        if s2=='?':
            if s1=='2':
                s2='3'
            else:
                s2='9'
        if s3=='?':
            s3='5'
        if s4=='?':
            s4='9'

        timef=s1+s2+':'+s3+s4

        # print(timef)
        return timef

s=Solution()
time = "?4:03"

s.maximumTime(time)



