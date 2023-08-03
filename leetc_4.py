#!/usr/bin/env python
# coding: utf-8

# Leet Code problem: 4


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        A = nums1
        B = nums2

        if len(A) > len(B):
            A, B = B, A

        # A is the smallest array
        l = 0
        r = len(A) - 1

        real_middle = (len(A) + len(B))//2

        while True:
            midA = (l + r)//2
            j = real_middle - midA -2 #left haf of B

            leftA = A[midA] if midA >= 0 else float('-inf')
            rightA = A[midA + 1] if (midA + 1) < len(A) else float('inf')
            leftB = B[j] if j >= 0 else float('-inf')
            rightB = B[j + 1] if (j + 1) < len(B) else float('inf') 

            if leftA <= rightB and leftB <= rightA:
                if (len(A) + len(B))%2 == 0:
                    return (max(leftA, leftB) + min(rightA, rightB))/2
                else:
                    return min(rightA, rightB)

            elif leftA > rightB:
                r = midA - 1
            else:
                l = midA + 1
