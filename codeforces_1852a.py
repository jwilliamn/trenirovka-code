#!/usr/bin/env python
# coding: utf-8

# Codeforces problem: 1852A


# Read variables from stdin
tests = int(input())
t = 0
while t < tests: 
    n, k = map(int, input().split())
    case = list(map(int, input().split()))
    #case = [int(a) for a in input().split()]

    j = 0
    min_val = 1

    while k > 0:
        while j < n and case[j] <= min_val + j:
            j += 1
        min_val += j

        k -=1
    t += 1


    print(min_val)
