#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# @lc code=start
# Definition for singly-linked list.
class Solution:
    def get_last_and_pop(self, head: Optional[ListNode]) -> ListNode:
        if head.next is None:
            return head
        if head.next.next is None:
            tmp = head.next
            head.next = None
            return tmp
        return self.get_last_and_pop(head.next)

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head.next:
            return None
        if head.next.next:
            tmp = ListNode(head.next.val, head.next.next)
            head.next = self.get_last_and_pop(head.next)
            head.next.next = tmp
            self.reorderList(head.next.next)


# @lc code=end
