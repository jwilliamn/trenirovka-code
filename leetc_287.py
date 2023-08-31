#!/usr/bin/env python
# coding: utf-8

# Leet Code problem: 287

# Sol; T O(n), M O(n)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        unique = set()

        i = 0
        while i < len(nums):
            if nums[i] in unique:
                return nums[i]
            
            unique.add(nums[i])
            i += 1