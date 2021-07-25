'''
-*- coding: utf-8 -*-
@Author  : zoeyzhu
@Time    : 2021/7/23 10:13 下午
@Software: PyCharm
@File    : 1893.py
@function:
1893. 检查是否区域内所有整数都被覆盖
给你一个二维整数数组 ranges 和两个整数 left 和 right 。每个 ranges[i] = [starti, endi] 表示一个从 starti 到 endi 的 闭区间 。

如果闭区间 [left, right] 内每个整数都被 ranges 中 至少一个 区间覆盖，那么请你返回 true ，否则返回 false 。

已知区间 ranges[i] = [starti, endi] ，如果整数 x 满足 starti <= x <= endi ，那么我们称整数x 被覆盖了。
输入：ranges = [[1,2],[3,4],[5,6]], left = 2, right = 5
输出：true
解释：2 到 5 的每个整数都被覆盖了：
- 2 被第一个区间覆盖。
- 3 和 4 被第二个区间覆盖。
- 5 被第三个区间覆盖。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/check-if-all-the-integers-in-a-range-are-covered
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
def get_fi(ele):
    return ele[0]
class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        1.
        """
        flag=1
        ranges.sort(key=get_fi)

        for item in ranges:
            key=item
            key_left=key[0]
            key_right=key[1]
            if left>=key_left and left<=key_right:
                if right<=key_right:
                    return True
                else:
                    if left==key_right:
                        left=left+1
                    else:
                        left=key_right+1
            else:
                if right <= key_right and right>=key_left:
                    if right==key_left:
                        right=right-1
                    right=key_left-1
                else:

                    continue
        return False


s=Solution()
list=[[15,36],[15,23],[15,44],[30,49],[2,19],[27,36],[7,42],[12,41]]

print(s.isCovered(list,19,47))