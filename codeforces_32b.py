#!/usr/bin/env python
# coding: utf-8

# Codeforces problem: 32B


# Read variables from stdin
coded = input()
alph = {'.':'0','-.':'1','--':'2'}

decoded = []

i, j = 0, 0
while i < len(coded):
    
    while coded[i:j] not in alph:
        j += 1

    if coded[i:j] in alph:
        decoded.append(alph[coded[i:j]])
        i = j

print(''.join(decoded))