# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 12:34:30 2020

@author: skyst
"""

class Solution:
    def isValid(self, s):
        stack = []
        pmap = {'(':')', '[':']','{':'}'}
        bplist = ['(','[','{']
        for c in s:
            if c in bplist:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                if pmap[stack[-1]] != c:
                    return False
                else:
                    stack.pop()
        if len(stack) > 0:
            return False
        else:
            return True
            
print( Solution().isValid('[](){}'))