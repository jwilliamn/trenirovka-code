#!/usr/bin/env python
# coding: utf-8

# Leet Code problem: 153


# Slow
# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         low = 0
#         high = len(nums) - 1

#         min_val = min(nums[low], nums[high])
#         while low <= high:

#             mid = (low + high)//2
#             #print(low, high)
#             #print(min_val)
#             if min_val == nums[low]:
#                 return min_val 
#             elif nums[low] > min_val:
#                 if nums[mid] > min_val:
#                     low = mid + 1
#                 else: 
#                     min_val = nums[mid]
#                     high = mid - 1
#             else:
#                 if nums[mid] > min_val:
#                     low = mid + 1
#                 else: 
#                     min_val = nums[mid]
#                     high = mid - 1
#             #print(min_val)
#         return min_val

# Faster
class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1

        min_val = min(nums[low], nums[high])
        while low <= high:
            if nums[low] < nums[high]:
                return min(min_val, nums[low])
            
            mid = (low + high)//2
            min_val = min(min_val, nums[mid])
            if nums[mid] >= nums[low]:
                low = mid + 1
            else:
                high = mid - 1

        return min_val

    