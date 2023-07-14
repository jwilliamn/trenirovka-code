#!/usr/bin/env python
# coding: utf-8

# Leet Code problem: 875


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        k = high
        while low <= high:
            mid = (high + low)//2
            time = 0
            for p in piles:
                if p % mid == 0:
                    time += (p//mid)
                else:
                    time += (p//mid) + 1
            
            if time <= h:
                k = min(k, mid)
                high = mid - 1
            else:
                low = mid + 1

        return k
    