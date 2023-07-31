#!/usr/bin/env python
# coding: utf-8

# Leet Code problem: 33


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        h = len(nums) - 1

        while l <= h:
            m = (l + h)//2
            if nums[m] == target:
                return m
            
            if nums[l] == target:
                return l
            if nums[h] == target:
                return h
                
            left = False
            right = False
            if nums[m] > nums[l]:
                left = True
            if nums[m] < nums[h]: 
                right = True

            if left and nums[l] > target:
                l = m + 1
            else:
                l = l + 1

            if right and nums[h] < target:
                h = m - 1
            else:
                h = h - 1

        return -1

    