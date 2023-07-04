#!/usr/bin/env python
# coding: utf-8

# Leet Code problem: 84


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largestArea = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                ix, he = stack.pop()
                largestArea = max(largestArea, he * (i - ix))
                start = ix

            stack.append((start, h))

        for i, h in stack:
            largestArea = max(largestArea, h * (len(heights) - i))

        return largestArea
