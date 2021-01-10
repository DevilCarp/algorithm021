#!/Users/lyjsmac/opt/anaconda3/bin/python3.8
# -*- encoding: utf-8 -*-
'''
@File    :   n叉树的前序遍历.py
@Time    :   2021/1/10 9:11 下午
@Author  :   little_carp
@Contact :   woshiliyujian@gmail.com
@Desc    :   None
'''

# here put the import lib
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


# 递归的方法
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return []

        list = []
        # 前序遍历的顺序为 根节点-左节点-右节点
        list.append(root.val)
        if root.children:
            for item in root.children:
                list += self.preorder(item)
        return list