#!/Users/lyjsmac/opt/anaconda3/bin/python3.8
# -*- encoding: utf-8 -*-
'''
@File    :   多数元素.py
@Time    :   2020/12/28 4:45 下午
@Author  :   little_carp
@Contact :   woshiliyujian@gmail.com
@Desc    :   None
'''

# here put the import lib
'''
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于⌊ n/2 ⌋的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。



示例1:

输入: [3,2,3]
输出: 3
示例2:

输入: [2,2,1,1,1,2,2]
输出: 2

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/majority-element
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 先遍历数组，构建hashmap,如{3: 2, 2: 1}
        num_dict = {}
        for i in nums:
            if i in num_dict:
                num_dict[i] +=1
            else:
                num_dict[i] =1
        # 判断条件：数组长度/2
        for i in num_dict.keys():
            if num_dict[i]> (len(nums)/2):
                return i