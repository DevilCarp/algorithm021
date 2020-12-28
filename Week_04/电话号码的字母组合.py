#!/Users/lyjsmac/opt/anaconda3/bin/python3.8
# -*- encoding: utf-8 -*-
'''
@File    :   电话号码的字母组合.py
@Time    :   2020/12/28 4:41 下午
@Author  :   little_carp
@Contact :   woshiliyujian@gmail.com
@Desc    :   None
'''

# here put the import lib
'''
给定一个仅包含数字2-9的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return list()

        # 构建字典
        dic_ = {}
        dic_['2'] = 'abc'
        dic_['3'] = 'def'
        dic_['4'] = 'ghi'
        dic_['5'] = 'jkl'
        dic_['6'] = 'mno'
        dic_['7'] = 'pqrs'
        dic_['8'] = 'tuv'
        dic_['9'] = 'wxyz'
        # 回溯函数~
        def backtrack(combination,nextdigit):
            if len(nextdigit)==0:
                res.append(combination)
            else:
                for letter in dic_[nextdigit[0]]:
                    backtrack(combination+letter,nextdigit[1:])
        res = []
        backtrack("",digits)
        return res