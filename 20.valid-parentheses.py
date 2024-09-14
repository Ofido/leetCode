#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
parenteses = (('(', ')'), ('{', '}'), ('[', ']'))
class Solution:
    def isValid(self, s: str) -> bool:
        return all([s.count(par[0]) == s.count(par[1]) for par in parenteses])
# @lc code=end

