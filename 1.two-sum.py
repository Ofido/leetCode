#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
import itertools


class Solution:
    def twoSum_1(self, nums: list[int], target: int) -> list[int]:
        for l in range(len(nums)):
            for r in range(len(nums)):
                if l == r:
                    continue
                if nums[l] + nums[r] == target:
                    return [l, r]
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        map = {val: idx for idx, val in enumerate(nums)}
        for idx, a in enumerate(nums):
            if (idx_map := map.get(target-a)) and idx_map != idx:
                return [idx,idx_map]
# @lc code=end

