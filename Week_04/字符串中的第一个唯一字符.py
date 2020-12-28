#!/Users/lyjsmac/opt/anaconda3/bin/python3.8
# -*- encoding: utf-8 -*-
'''
@File    :   字符串中的第一个唯一字符.py
@Time    :   2020/12/28 4:42 下午
@Author  :   little_carp
@Contact :   woshiliyujian@gmail.com
@Desc    :   None
'''

# here put the import lib
'''
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。


示例：

s = "leetcode"
返回 0

s = "loveleetcode"
返回 2

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/first-unique-character-in-a-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1
        # 利用python的Counter函数对字典进行计数
        str_dic = collections.Counter(s)
        for i in range(len(s)):
            if str_dic.get(s[i])==1:
                return i
        # 如出现Counter({'c': 2})的情况的话，是不存在唯一字符的，直接返回-1
        return -1