#!/Users/lyjsmac/opt/anaconda3/bin/python3.8
# -*- encoding: utf-8 -*-
'''
@File    :   最长公共子序列.py
@Time    :   2021/1/4 10:47 上午
@Author  :   little_carp
@Contact :   woshiliyujian@gmail.com
@Desc    :   None
'''

# here put the import lib
'''
给定两个字符串text1 和text2，返回这两个字符串的最长公共子序列的长度。

一个字符串的子序列是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。两个字符串的「公共子序列」是这两个字符串所共同拥有的子序列。

若这两个字符串没有公共子序列，则返回 0。

示例 1:

输入：text1 = "abcde", text2 = "ace" 
输出：3  
解释：最长公共子序列是 "ace"，它的长度为 3。
示例 2:

输入：text1 = "abc", text2 = "abc"
输出：3
解释：最长公共子序列是 "abc"，它的长度为 3。

'''


class Solution:
    def longestCommonSubsequence(self, A: str, B: str) -> int:
        dp = [0] * len(B)
        for a in A:
            mx = 0
            prev = dp[0]
            dp[0] = max(prev, a == B[0])
            for i in range(1, len(B)):
                mx = max(mx, prev)
                prev = dp[i]
                dp[i] = max(prev, (a == B[i]) + mx)

        return int(max(dp))