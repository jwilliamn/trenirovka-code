#!/usr/bin/env python
# coding: utf-8

# Leet Code problem: 19


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # Get the length of the linked list
        curr = head
        stack = []
        while curr:
            stack.append(curr)
            curr = curr.next

        # Populate the new linked list, skiping the n node
        new = ListNode(None)
        tmp = new

        curr = head
        i = 0
        while curr:
            nextp = curr.next
            if i == (len(stack) - n):               
                tmp2 = curr.next
                tmp.next = tmp2
            else:
                tmp.next = curr
                tmp = tmp.next
            curr = nextp

            i += 1

        return new.next
