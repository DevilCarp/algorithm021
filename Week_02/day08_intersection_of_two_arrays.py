# 两个数组的交集2
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1 = collections.Counter(nums1)
        num2 = collections.Counter(nums2)
        result = num1 & num2
        num = result.elements()
        return num