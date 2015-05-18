#!/usr/bin/python

class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        listOfWords = s.split()
        listOfWordsStripped = [i.strip() for i in listOfWords]
        return ' '.join(listOfWordsStripped[::-1])

s = Solution()
print s.reverseWords("the sky is blue")
