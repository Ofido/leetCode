#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# @lc code=start
# Definition for singly-linked list.
class Solution:
    def count_depth(self, head) -> int:
        return self.count_depth(head.next) + 1 if head.next else 1

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count_n = self.count_depth(head)
        if count_n != n:
            head.next = self.removeNthFromEnd(head.next, n)
            return head
        else:
            return head.next if head.next else None

    def removeNthFromEnd_best_recursion(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def removeNode(node, n):
            if not node:
                return 0
            cnt = removeNode(node.next, n)
            if cnt == n:
                node.next = node.next.next
            return cnt + 1

        return head.next if removeNode(head, n) == n else head


# @lc code=end
