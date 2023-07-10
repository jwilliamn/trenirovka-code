#!/usr/bin/env python
# coding: utf-8

# Leet Code problem: 74


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for li in matrix:
            low = 0
            high = len(li) - 1
            while low <= high:
                mid = (low + high)//2
                if li[mid] == target:
                    return True
                elif li[mid] < target:
                    low = mid + 1
                else: high = mid - 1

        return False
    