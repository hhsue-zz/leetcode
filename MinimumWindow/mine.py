#!/usr/bin/python

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {string}
    def minWindow(self, s, t):
        currStr = ''
        currMin = ''
        index = {}
        count = 0
        if len(s) < len(t):
            return ''
        for i in range(len(s)):
            currStr += s[i]
            if s[i] in t:
                index[s[i]] = i
                if len(index) == len(t):
                    count += 1
                    if currStr[0] == s[i]:
                        currStr = s[min(index.values()):]
                    if count == 1:
                        currMin = currStr
                    else:
                        print currStr
                        if len(currStr) < len(currMin):
                            currMin = currStr
        return currMin 
'''abbcbbbbbcbbbbbbbba
'''
            
s = 'ADOBECODEBANC'
t = 'ABC'
sol = Solution()
print sol.minWindow(s,t)

