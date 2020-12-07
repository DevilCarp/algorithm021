class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_ = len(nums)
        nums[:] = nums[len_-k:]+nums[0:len_-k]
        return nums
