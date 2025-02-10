#
# @lc app=leetcode id=3174 lang=python3
#
# [3174] Clear Digits
#


# @lc code=start
class Solution:
    def clearDigits(self, s: str) -> str:
        # Convert the string to a list for easier manipulation
        s_list = list(s)
        length = len(s_list)

        # Iterate through the list while there are still digits
        while True:
            found_digit = False
            for i in range(1, length):  # Start from 1 to ensure there's a character to the left
                if s_list[i].isdigit():
                    # Remove the current digit and the character to its left
                    del s_list[i-1:i+1]
                    length -= 2  # Update the length after the removal
                    found_digit = True
                    break  # Restart the check after modification

            if not found_digit:
                break  # Exit if no digits are found

        return "".join(s_list)  # Convert the list back to a string


# @lc code=end
