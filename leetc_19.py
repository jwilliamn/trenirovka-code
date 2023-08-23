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

# Slower but cleaner solution
# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         dummy=ListNode(-1,head)
        
#         # pointers
#         fast = head
#         slow = dummy
        
#         # Get fast to n
#         for i in range(n-1):
#             fast=fast.next
        
#         # Move forward until fast reaches None
#         while fast.next:
#             fast=fast.next
#             slow=slow.next

#         # Remove the n (from last) node
#         slow.next=slow.next.next
#         return dummy.next