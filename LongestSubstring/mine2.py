#!/usr/bin/python
# longest substring for string s 
# input s, return length of longest substring

class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        seenLetters = {}
        currStr = ''
        currMax = 0
        start = 0
        for i in range(len(s)):
            if s[i] in seenLetters:
                if seenLetters[s[i]] >= start:
                    currStr = s[seenLetters[s[i]]+1:i+1]
                    start = seenLetters[s[i]] + 1
                else:
                    currStr += s[i]
                seenLetters[s[i]] = i
            else:
                seenLetters[s[i]] = i
                currStr += s[i]
            currMax = len(currStr) if len(currStr) > currMax else currMax
            #print currStr
        return currMax

s=Solution()
substring = 'aaaaaa'
print 'the length of the longest substring of', substring, 'is', s.lengthOfLongestSubstring(substring)
