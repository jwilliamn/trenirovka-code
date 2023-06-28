#!/usr/bin/env python
# coding: utf-8

# Codeforces problem: 266B


# Read variables from stdin
n, t = map(int, input().split())
queue = input()

stack = []

i = 0
while i < n:
    if queue[i] == 'B':
        j = 0
        while j < t and i + j < n -1:
            if queue[i + j + 1] == 'G':
                stack.append('G')
                j += 1
            else: break
        stack.append('B')
        i = i + j + 1

    else: 
        stack.append('G')
        i += 1

print(''.join(stack))
