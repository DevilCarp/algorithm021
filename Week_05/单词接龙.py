#!/Users/lyjsmac/opt/anaconda3/bin/python3.8
# -*- encoding: utf-8 -*-
'''
@File    :   单词接龙.py
@Time    :   2021/1/4 10:35 上午
@Author  :   little_carp
@Contact :   woshiliyujian@gmail.com
@Desc    :   None
'''

# here put the import lib
'''
给定两个单词（beginWord和 endWord）和一个字典，找到从beginWord 到endWord 的最短转换序列的长度。转换需遵循如下规则：

每次转换只能改变一个字母。
转换过程中的中间单词必须是字典中的单词。
说明:

如果不存在这样的转换序列，返回 0。
所有单词具有相同的长度。
所有单词只由小写字母组成。
字典中不存在重复的单词。
你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
示例1:

输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

输出: 5

解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
     返回它的长度 5。
示例 2:

输入:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

输出:0

解释:endWord "cog" 不在字典中，所以无法进行转换。

'''
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # 利用BFS来解题
        # 建立通用list
        size , general_dic = len(beginWord),collections.defaultdict(list)
        for w in wordList:
            for _ in range(size):
                general_dic[w[:_]+"*"+w[_+1:]].append(w)
        # defaultdict(<class 'list'>, {'*ot': ['hot', 'dot', 'lot'], 'h*t': ['hot'], 'ho*': ['hot'], 'd*t': ['dot'], 'do*': ['dot', 'dog'], '*og': ['dog', 'log', 'cog'], 'd*g': ['dog'], 'l*t': ['lot'], 'lo*': ['lot', 'log'], 'l*g': ['log'], 'c*g': ['cog'], 'co*': ['cog']})

        # BFS
        # 构建deque双端队列
        queue = deque()
        queue.append((beginWord,1)) # BFS中，queue中通常混合多层的node，无法区分层，要区分层就要在queue中直接加入当前node所属层数
        mark_dic = defaultdict(bool) # bool的默认值是false，因此所有不在list里的是false
        mark_dic[beginWord] = True
        while queue:
            cur_word ,level = queue.popleft() # queue头弹出一个
            for i in range(size): #找邻居，邻居都在level+1层
                for neighbour in general_dic[cur_word[:i]+"*"+cur_word[i+1:]]:
                    if neighbour ==endWord:return level+1
                    if not mark_dic[neighbour] :
                        mark_dic[neighbour] = True
                        queue.append((neighbour, level+1))#符合条件(neighbour + unmarked) 进去
        return 0