#!/usr/bin/env python
# coding: utf-8

# Codeforces problem: 266B


# Read variables from stdin
n, t = map(int, input().split())
queue = input()


j = 0
while j < t:
    i = 0
    stack = []
    while i < n:
        if queue[i] == 'B' and i < n - 1 and queue[i + 1] == 'G':
            stack.append('G')
            stack.append('B')
            i = i + 2

        else: 
            stack.append(queue[i])
            i += 1

    queue = ''.join(stack)
    j += 1

print(''.join(stack))
