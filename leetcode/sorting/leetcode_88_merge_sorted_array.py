# leetcode_88: https://leetcode.com/problems/merge-sorted-array/description
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(n):
            nums1[m +i] = nums2[i]
        nums1.sort()
