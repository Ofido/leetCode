#
# @lc app=leetcode id=3264 lang=python3
#
# [3264] Final Array State After K Multiplication Operations I
#


# @lc code=start
class Solution:
    def getFinalState(self, nums: list[int], k: int, multiplier: int) -> list[int]:
        for _ in range(k):
            idx = nums.index(min(nums))
            nums[idx] *= multiplier
        return nums


# @lc code=end
