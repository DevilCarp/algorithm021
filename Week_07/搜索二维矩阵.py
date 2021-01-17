#!/Users/lyjsmac/opt/anaconda3/bin/python3.8
# -*- encoding: utf-8 -*-
'''
@File    :   搜索二维矩阵.py
@Time    :   2021/1/17 11:03 下午
@Author  :   fancycarp
@Contact :   woshiliyujian@gmail.com
@Desc    :   None
'''

# here put the import lib
'''
编写一个高效的算法来判断m x n矩阵中，是否存在一个目标值。该矩阵具有如下特性：

每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。


示例 1：


输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
输出：true
示例 2：


输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
输出：false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-a-2d-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # 对于二维数组，可以转换为一维有序数组，来进行二分查找法
        m  = len(matrix) # 看存在多少组有序短数组
        if m==0:
            return False
        n = len(matrix[0]) # 有序短数组的长度

        # 进行二分查找法
        left,right = 0,m*n-1  # 定义一维有序数组的左右边界
        while left<=right:# 迭代
            pivot_idx = (left+right)//2 # 除数取整
            # 通过行列来定义该元素的在原matrix中的位置
            pivot_element = matrix[pivot_idx//n][pivot_idx%n] # row\col
            if target ==pivot_element:
                return True
            else:
                if target<pivot_element:
                    right  = pivot_idx-1
                else:
                    left = pivot_idx +1
        return False