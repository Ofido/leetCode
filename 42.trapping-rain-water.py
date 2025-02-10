#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
# explain:
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
# @lc code=start
class Solution:
    def trap(self, height: list[int]) -> int:
        last_pos = 0
        next_low: list[int] = []
        water = 0
        end = len(height)
        for h in range(len(height)):
            print(f"{height[h]=}")
            if height[h] == 0 and len(next_low) == 0 and last_pos == 0:
                print("None")
                continue
            if last_pos <= height[h] or h == end:
                print("hi")
                if len(next_low) == 0:
                    print("first | reset")
                    last_pos = height[h]
                    continue
                lower_water = last_pos if last_pos <= height[h] else height[h]
                print(f"{lower_water=}")
                for w in next_low:
                    print(f"add {lower_water - w=}")
                    water += lower_water - w
                print("reset")
                last_pos = height[h]
                next_low = []
                continue
            print("only appended")
            next_low.append(h)
        if len(next_low) > 1:
            print("Second Chance")
            water += self.trap(next_low)
        return water


# @lc code=end
# tenho que validar o primeiro numero e o proximo numero >= e calcular a gua entre eles
