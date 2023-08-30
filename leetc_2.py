#!/usr/bin/env python
# coding: utf-8

# Leet Code problem: 2


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        result = ListNode()
        tmp = result
        carry = 0

        while l1 or l2:
            if not l1:
                l1val = 0
            else:   
                next1 = l1.next
                l1val = l1.val
            if not l2:
                l2val = 0
            else:   
                next2 = l2.next
                l2val = l2.val
            
            # sum 
            sumnode = l1val + l2val + carry
            val = sumnode%10
            carry = sumnode//10

            # new node
            tmp.next = ListNode(val)
            tmp = tmp.next
            
            # update linked lists
            l1 = next1
            l2 = next2

        if carry == 1:
            tmp.next = ListNode(1)

        return result.next