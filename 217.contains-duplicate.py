#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate_easiest(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))

    def containsDuplicate(self, nums: list[int]) -> bool:
        countNumbers = set()
        for number in sorted(nums):
            if number not in countNumbers:
                countNumbers.add(number)
            else:
                return True
        return False
# @lc code=end

