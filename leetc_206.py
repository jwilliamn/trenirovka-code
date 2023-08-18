#!/usr/bin/env python
# coding: utf-8

# Leet Code problem: 206


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Iteratively
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         prev = None
#         curr = head

#         while curr:
#             next_p = curr.next
#             curr.next = prev
#             prev = curr
#             curr = next_p

#         return prev

# Recursively
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
#         if head == None or head.next == None:
#             return head

#         new_head = self.reverseList(head.next)
#         head.next.next = head
#         head.next = None

#         return new_head

# Recursively 2
class Solution:
    def reverseList(self, head: Optional[ListNode], prev=None) -> Optional[ListNode]:
        if head == None: return prev

        next_head = head.next
        head.next = prev
        return self.reverseList(next_head, head)
            
