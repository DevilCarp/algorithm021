#!/Users/lyjsmac/opt/anaconda3/bin/python3.8
# -*- encoding: utf-8 -*-
'''
@File    :   x的平方根.py
@Time    :   2020/12/28 4:46 下午
@Author  :   little_carp
@Contact :   woshiliyujian@gmail.com
@Desc    :   None
'''

# here put the import lib
'''
实现int sqrt(int x)函数。

计算并返回x的平方根，其中x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:

输入: 4
输出: 2
示例 2:

输入: 8
输出: 2
说明: 8 的平方根是 2.82842..., 
    由于返回类型是整数，小数部分将被舍去。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sqrtx
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def mySqrt(self, x: int) -> int:
        # 方法一：二分查找法
        left,right = 0,x
        while left <=right :
            mid = left + (right - left) //2
            # 让中间数来进行平方，与原数进行比较
            mid_square  = mid**2
            if mid_square ==x:
                return mid
            elif  mid_square > x:
                right = mid-1
            else:
                left = mid+1
        return min(left,right)


        # 方法二：牛顿迭代法