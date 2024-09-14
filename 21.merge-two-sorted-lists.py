#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# @lc code=start
# Definition for singly-linked list.


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        return (
            ListNode(list1.val, self.mergeTwoLists(list1.next, list2))
            if list1 is not None and list1.val < list2.val
            else ListNode(list2.val, self.mergeTwoLists(list2.next, list1))
        )


# @lc code=end
