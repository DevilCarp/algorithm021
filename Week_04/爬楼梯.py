#!/Users/lyjsmac/opt/anaconda3/bin/python3.8
# -*- encoding: utf-8 -*-
'''
@File    :   爬楼梯.py
@Time    :   2020/12/28 4:39 下午
@Author  :   little_carp
@Contact :   woshiliyujian@gmail.com
@Desc    :   None
'''

# here put the import lib
'''
假设你正在爬楼梯。需要 n阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/climbing-stairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def climbStairs(self, n: int) -> int:
        # 方法一，通过递归的方式(超时)
        # if n <=2 :
        #     return n
        # return self.climbStairs(n-1)+self.climbStairs(n-2)

        # 方法二，通过字典的形式
        # dp  ={}
        # dp[1] = 1
        # dp[2] = 2
        # for i in range(3,n+1):
        #     dp[i] = dp[i-1]+dp[i-2]
        # return dp[n]

        # 方法三、不通过字典的形式
        if n <= 2:
            return n
        x = 1
        y = 2
        for i in range(3, n + 1):
            z = x + y
            x = y
            y = z
        return y