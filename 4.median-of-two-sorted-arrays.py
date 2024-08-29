#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
from statistics import median
from typing import List


# @lc code=start
class Solution:
    def findMedianSortedArrays_easy(self, nums1: List[int], nums2: List[int]) -> float:
        return median(nums1 + nums2)

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        data = sorted(nums1 + nums2)
        n = len(data)
        if n & 1:
            return data[n // 2]
        else:
            i = n // 2
            return (data[i - 1] + data[i]) / 2

    def findMedianSortedArrays_sla(self, nums1: List[int], nums2: List[int]) -> float:
        i, j = 0, 0
        last_n = 0

        # Percorre ambas as listas e compara os elementos
        while (i < len(nums1) - 1 and j < len(nums2) - 1) or i + j < len(nums1) + len(nums2):
            print(f"{i=}")
            print(f"{j=}")
            print(f"{i+j=}")
            print(f"{len(nums1) + len(nums2)=}")
            print(f"{(i + j) < (len(nums1) + len(nums2))=}")
            if nums1[i] < nums2[j]:
                last_n = nums1[i]
                i += 1
            else:
                last_n = nums2[j]
                j += 1

        if (len(nums1) + len(nums2)) & 1 == 0:
            print(f"{i=}")
            print(f"{j=}")
            print(f"{last_n=}")
            print(f"{nums1[i]=}")
            print(f"{nums2[j]=}")

        return last_n


# @lc code=end
