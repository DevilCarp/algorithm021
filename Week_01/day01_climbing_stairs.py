class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n ==1 or n==2:
            return n
        x = 1# 一楼开始爬的方法数 
        y = 2# 二楼开始爬的方法数
        z = 0# 初始化总方法数
        # 从三楼开始爬
        for i in range(2,n):
            # 总方法数为n-1和n-2的方法数之和
            z = x+y
            # 动态推导
            x = y
            y = z
        return z
