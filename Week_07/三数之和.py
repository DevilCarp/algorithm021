#!/Users/lyjsmac/opt/anaconda3/bin/python3.8
# -*- encoding: utf-8 -*-
'''
@File    :   三数之和.py
@Time    :   2021/1/17 11:07 下午
@Author  :   fancycarp
@Contact :   woshiliyujian@gmail.com
@Desc    :   None
'''

# here put the import lib
'''
给你一个包含 n 个整数的数组nums，判断nums中是否存在三个元素 a，b，c ，使得a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。


示例 1：

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
示例 2：

输入：nums = []
输出：[]
示例 3：

输入：nums = [0]
输出：[]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 另 a+b+c=0  , 即为 a+b=-c
        res = []
        # 先对列表元素进行从小到大的排序
        nums.sort()
        for i in xrange(len(nums)-2):
            if i >0 and nums[i] ==nums[i-1]:#等于前一个元素时，跳过继续
                continue
            l,r  = i+1,len(nums)-1 # 定义左右指针
            while l<r:
                s = nums[i] + nums[l]+ nums[r] #此时三数之和小于0，从起始开始夹逼
                if s<0: #如果s小于0 ，说明l元素过小（排序过，所以左小右大）
                    l +=1
                elif s>0:#如果s小于0 ，说明r元素过大（排序过，所以左小右大）
                    r -=1
                else: # 三数之和为0，加入结果列表
                    res.append([nums[i],nums[l],nums[r]])
                    # 在等于0的情况中，继续左右夹逼（如果下一步与该元素相同的话）
                    while l<r and nums[l] ==nums[l+1]:
                        l +=1
                    while l<r and nums[r] ==nums[r-1]:
                        r -=1
                    # 继续夹逼
                    l +=1
                    r -=1
        return res
