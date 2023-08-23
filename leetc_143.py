#!/usr/bin/env python
# coding: utf-8

# Leet Code problem: 143


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # # find the second half
        # slow, fast = head, head.next
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next

        # # traverse the second half
        # second = slow.next
        # prev = slow.next = None
        # while second:
        #     nextp = second.next
        #     second.next = prev
        #     prev = second
        #     second = nextp

        # # merge the second and first half
        # first, second = head, prev
        # while second:
        #     t1, t2 = first.next, second.next
        #     first.next = second
        #     second.next = t1
        #     first, second = t1, t2

        curr = head
        stack = []
        while curr:
            stack.append(curr)
            curr = curr.next

        curr = head
        for i in range(len(stack)//2):
            tmp = curr.next
            s = stack.pop()
            curr.next = s
            s.next = tmp
            curr = tmp
        
        if curr:
            curr.next = None