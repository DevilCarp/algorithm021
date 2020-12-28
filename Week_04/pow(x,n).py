#!/Users/lyjsmac/opt/anaconda3/bin/python3.8
# -*- encoding: utf-8 -*-
'''
@File    :   pow(x,n).py
@Time    :   2020/12/28 4:38 下午
@Author  :   little_carp
@Contact :   woshiliyujian@gmail.com
@Desc    :   None
'''

# here put the import lib
'''
实现pow(x, n)，即计算 x 的 n 次幂函数。

示例 1:

输入: 2.00000, 10
输出: 1024.00000
示例2:

输入: 2.10000, 3
输出: 9.26100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/powx-n
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if n == 0: return 1
            if n == 1: return x

            if n % 2:
                return helper(x * x, n // 2) * x
            else:
                return helper(x * x, n // 2)

        if n < 0:
            return 1 / self.myPow(x, -n)

        if x == 0: return 0

        if x > 0 or n % 2 == 0:
            sign = 1
        else:
            sign = -1

        x = abs(x)
        return sign * helper(x, n)