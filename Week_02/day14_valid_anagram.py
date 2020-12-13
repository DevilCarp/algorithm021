class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # python直接比较两个字典计数
        return True if collections.Counter(s) == collections.Counter(t) else False