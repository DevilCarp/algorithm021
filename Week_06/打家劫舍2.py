#!/Users/lyjsmac/opt/anaconda3/bin/python3.8
# -*- encoding: utf-8 -*-
'''
@File    :   打家劫舍2.py
@Time    :   2021/1/10 9:10 下午
@Author  :   little_carp
@Contact :   woshiliyujian@gmail.com
@Desc    :   None
'''

# here put the import lib
'''
你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。

给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，能够偷窃到的最高金额。

示例1：

输入：nums = [2,3,2]
输出：3
解释：你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
示例 2：

输入：nums = [1,2,3,1]
输出：4
解释：你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
    偷窃到的最高金额 = 1 + 3 = 4 。
示例 3：

输入：nums = [0]
输出：0

'''
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def robmax(nums):
            nums_len = len(nums)
            # 先列明特殊情况
            if not nums:
                return 0
            if nums_len ==1:
                return nums[0]
            # 构建状态列表
            opt = [0] * nums_len
            opt[0] = nums[0]
            opt[1] = max(nums[0],nums[1])

            for i in range(2,nums_len):
                opt[i] = max(opt[i-1],opt[i-2]+nums[i])
            return opt[nums_len-1]
        if not nums:
            return 0
        if len(nums) ==1:
            return nums[0]
        nums1 = nums[1:] # 从1到n找到最大值
        nums2 = nums[0:len(nums)-1] # 从0到n-1找到最大值
        # 最终返回(1,n) 和 (0,n-1)两个最大值中大的
        return max(robmax(nums1),robmax(nums2))