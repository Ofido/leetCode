#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#


# @lc code=start
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        high = nums[0]
        cnt = 1
        while high < nums[-1]:
            if high == nums[cnt]:
                nums.pop(cnt)
            else:
                high = nums[cnt]
                cnt += 1
        while cnt < len(nums):
            nums.pop(cnt)
        return len(nums)

    def removeDuplicatesPythonic(self, nums: list[int]) -> int:
        nums[:] = sorted(set(nums))
        return len(nums)


# @lc code=end
