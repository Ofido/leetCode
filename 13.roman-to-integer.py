#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#


# @lc code=start
class Solution:
    # values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    # def romanToInt_one_line(self, s: str) -> int:
    #     return sum(
    #         (
    #             -self.values.get(s[a])
    #             if a + 1 < len(s) and self.values[s[a]] < self.values[s[a + 1]]
    #             else self.values.get(s[a])
    #         )
    #         for a in range(len(s))
    #     )

    # def romanToInt_poor(self, s: str) -> int:
    #     ans = 0
    #     for i in range(len(s)):
    #         if i < len(s) - 1 and self.values[s[i]] < self.values[s[i + 1]]:
    #             ans -= self.values[s[i]]
    #         else:
    #             ans += self.values[s[i]]

    #     return ans

    def romanToInt(self, s: str) -> int:
        values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        return sum(
            values.get(a)
            for a in s.replace("IV", "IIII")
            .replace("IX", "VIIII")
            .replace("XL", "XXXX")
            .replace("XC", "LXXXX")
            .replace("CD", "CCCC")
            .replace("CM", "DCCCC")
        )

    # def romanToInt_nha(self, s: str) -> int:
    #     translations = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    #     number = 0
    #     s = s.replace("IV", "IIII").replace("IX", "VIIII")
    #     s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
    #     s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
    #     for char in s:
    #         number += translations[char]
    #     return number

    def romanToInt_wft(self, s: str) -> int:
        symbol = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        n = len(s)
        ans = 0
        prev = None
        for i in range(n - 1, -1, -1):
            curr = s[i]
            if prev and symbol[curr] < prev:
                ans -= symbol[curr]
                prev = None
            else:
                ans += symbol[curr]
                prev = symbol[curr]
        return ans


# @lc code=end
