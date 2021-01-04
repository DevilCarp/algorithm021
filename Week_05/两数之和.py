#!/Users/lyjsmac/opt/anaconda3/bin/python3.8
# -*- encoding: utf-8 -*-
'''
@File    :   两数之和.py
@Time    :   2021/1/4 10:45 上午
@Author  :   little_carp
@Contact :   woshiliyujian@gmail.com
@Desc    :   None
'''

# here put the import lib
'''
给定一个整数数组 nums和一个整数目标值 target，请你在该数组中找出 和为目标值 的那两个整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

你可以按任意顺序返回答案。



示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 最终返回的是x 和y的索引位置
        hash_map={}
        for loc,num in enumerate(nums):
            hash_map[num] = loc
        for i ,num in enumerate(nums):
            j = hash_map.get(target-num)
            if j is not None and i != j:
                return[i,j]
