#!/usr/bin/env python
# coding: utf-8

# Leet Code problem: 138


"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashmap = {None:None}

        # Create a copy of nodes and hashmap
        curr = head
        while curr:
            copy = Node(curr.val)
            hashmap[curr] = copy
            curr = curr.next

        # conect the pointers
        curr = head
        while curr:
            copy = hashmap[curr]
            copy.next = hashmap[curr.next]
            copy.random = hashmap[curr.random]
            curr = curr.next

        return hashmap[head]