#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        print(f"isHappy?: {n=}")
        if n < 10:
            return n == 1
        return self.isHappy(sum(map(lambda x: x*x, map(int, str(n)))))
# @lc code=end

