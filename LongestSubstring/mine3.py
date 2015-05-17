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
        for i in range(len(s)):
            if s[i] in seenLetters:
                if s[i] in currStr:
                    currStr = s[seenLetters[s[i]]+1:i+1]
                else:
                    currStr += s[i]
                seenLetters[s[i]] = i
            else:
                seenLetters[s[i]] = i
                currStr += s[i]
            currMax = len(currStr) if len(currStr) > currMax else currMax
        return currMax

s=Solution()
substring = 'aaaaaa'
print 'the length of the longest substring of', substring, 'is', s.lengthOfLongestSubstring(substring)
substring = 'tmmzuxt'
print 'the length of the longest substring of', substring, 'is', s.lengthOfLongestSubstring(substring)
