#!/Users/lyjsmac/opt/anaconda3/bin/python3.8
# -*- encoding: utf-8 -*-
'''
@File    :   最小路径和.py
@Time    :   2021/1/17 11:02 下午
@Author  :   fancycarp
@Contact :   woshiliyujian@gmail.com
@Desc    :   None
'''

# here put the import lib
'''
给定一个包含非负整数的 mxn网格grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。


示例 1：


输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
输出：7
解释：因为路径 1→3→1→1→1 的总和最小。
示例 2：

输入：grid = [[1,2,3],[4,5,6]]
输出：12

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-path-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # i 是代表行的长度
        # j 是代表列的长度
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == j ==0: # 起点位置
                    continue
                elif i == 0 : #只能往下走
                    grid[i][j] = grid[i][j-1] + grid[i][j]
                elif j ==0 : #只能往右走
                    grid[i][j] = grid[i-1][j]+grid[i][j]
                else :
                    grid[i][j] = grid[i][j] + min(grid[i-1][j],grid[i][j-1])
        # 是在原grid的基础上，直接按dp的动态结果进行了覆盖，所以二维数组的最后一个值，就是走到最后一个点的最小数字之和
        return grid[-1][-1]