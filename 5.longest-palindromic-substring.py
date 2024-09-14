#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
from itertools import combinations


# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        for a in range(len(s), 0, -1):
            for c in combinations(s, a):
                if c == c[::-1]:
                    return ''.join(c)
        return s[0]


# @lc code=end
