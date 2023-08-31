#!/usr/bin/env python
# coding: utf-8

# Leet Code problem: 141


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Hash method
# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         set_heads = set()

#         while head:
#             nextn = head.next
#             if head in set_heads:
#                 return True
#             set_heads.add(head)

#             head = nextn
            
#         return False

# Floyd's algorithm (faster algo)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            head = head.next
            if head == fast:
                return True
        return False

