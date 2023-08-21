#!/usr/bin/env python
# coding: utf-8

# Leet Code problem: 21


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1:
            return list2
        elif not list2:
            return list1
        else:
            tmp = ListNode()
            merged = tmp
            while list1 and list2:
                if list1.val < list2.val:
                    merged.next =  list1
                    list1 = list1.next
                else:
                    merged.next = list2
                    list2 = list2.next
                #print(merged.next)
                merged = merged.next
            if list1:
                merged.next = list1
            else:
                merged.next = list2

        return tmp.next

            
