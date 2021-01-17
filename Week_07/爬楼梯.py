#!/Users/lyjsmac/opt/anaconda3/bin/python3.8
# -*- encoding: utf-8 -*-
'''
@File    :   爬楼梯.py
@Time    :   2021/1/17 11:08 下午
@Author  :   fancycarp
@Contact :   woshiliyujian@gmail.com
@Desc    :   None
'''

# here put the import lib
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n

        x = 0
        y = 1
        z = 1
        for i in range(2, n + 1):
            x, y = y, z
            z = x + y
        return z