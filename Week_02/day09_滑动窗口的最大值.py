class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        lenth = len(nums)
        if not nums:
            return result
        for i in range(lenth-k+1):
            result.append(max(nums[i:i+k:1]))
        return result