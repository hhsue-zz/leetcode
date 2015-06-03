#!/usr/bin/python

# Write a function to find the longest common prefix string amongst an array of strings.

class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        i = 0
        if not strs:
            return ''
        minStr = min(strs, key=len)
        lenMinStr = len(minStr)
        while i < lenMinStr:
            currLetter = minStr[i]
            for s in strs:
                if s[i] != currLetter:
                    return minStr[:i]
            i += 1
        return minStr
        
            

s = Solution()
print s.longestCommonPrefix(['asdf','asd','asdfwergerg'])

# make sure strings
# 
