#!/usr/bin/python

class Solution:
    # @param {string} s
    # @return {boolean}
    def isPalindrome(self, s):
        alphanumeric = ''.join([letter.lower() for letter in s if letter.isalnum()])
        return alphanumeric[::-1] == alphanumeric
        


s = Solution()
print s.isPalindrome("A man, a plan, a canal: Panama")
print s.isPalindrome("asdfjiejfwe awefawe.a wef.aw.efa .")
