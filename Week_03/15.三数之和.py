#
# @lc app=leetcode.cn id=15 lang=python
#
# [15] 三数之和
#

# @lc code=start
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 两数之和是 a+b = 9 ，9是一个固定的值
        # 三数之和是一个动态的值，即a+b = -c
        # 通过枚举加双指针的方式来完成

        n = len(nums)
        nums.sort()
        ans = []

        # 枚举a
        for first in range(n):
            # 要和上次枚举的数值不相同
            if first > 0 and nums[first] == nums[first-1]:
                continue
            # c对应 指针初试指向数组的最右端
            third = n-1
            target = -nums[first]
            # 枚举b
            for second in range(first+1, n):
                # 需要和上次枚举的数不相同
                if second > first + 1 and nums[second] == nums[second-1]:
                    continue
                # 需要保证b的指针在c的指针的左侧
                while second < third and nums[second] + nums[third] > target:
                    third -=1  
                # 如果指针重合 随着b后续的增加
                # 就不会满足a+b+c=0 并且b<c的c了，可退出循环
                if second ==third:
                    break
                if nums[second] + nums[third] == target:
                    ans.append([nums[first],nums[second],nums[third]])
        return ans

# @lc code=end
