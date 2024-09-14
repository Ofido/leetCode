#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# @lc code=start
# Definition for singly-linked list.


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode], maior_que_10: bool = False
    ) -> ListNode | None:
        result = l1.val + l2.val + maior_que_10
        if l1.next is None and l2.next is None:
            return ListNode(result % 10, None if result < 10 else ListNode(1, None))
        if l1.next is None:
            return ListNode(result % 10, self.addTwoNumbers(ListNode(0, None), l2.next, result >= 10))
        if l2.next is None:
            return ListNode(result % 10, self.addTwoNumbers(l1.next, ListNode(0, None), result >= 10))
        return ListNode(result % 10, self.addTwoNumbers(l1.next, l2.next, result >= 10))


# @lc code=end
