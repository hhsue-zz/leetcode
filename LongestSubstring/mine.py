#!/usr/bin/python
# longest substring for string s 
# input s, return length of longest substring

class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        savedPatterns = {}
        for i in range(len(s)):
            currentString = ''
            for j in range(i,len(s)):
                currentString += s[j]
                if currentString in savedPatterns:
                    savedPatterns[currentString] += 1
                else:
                    savedPatterns[currentString] = 1
        singularOccurences = {k:v for (k,v) in savedPatterns.iteritems() if v == 1}
        return singularOccurences
        #return max(singularOccurences, key=lambda k: singularOccurences.keys())

s=Solution()
print s.lengthOfLongestSubstring('basdfasdf')
