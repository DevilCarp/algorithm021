"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root == None:
            return []
        ret = [root.val]
        for i in root.children:
            ret.extend(self.preorder(i))
        return ret