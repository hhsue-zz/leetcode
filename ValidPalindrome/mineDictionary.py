#!/usr/bin/python

class Solution:
    # @param {string} s
    # @return {boolean}
    def isPalindrome(self, s):
        # remove all symbols, and lower case
        # write string backwards without spaces
        # compare with original without spaces
        s = s.encode('ascii','ignore')
        words_only = ''
        dictionary = {}
        for letter in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789':
            dictionary[letter] = 1 
        alphanumeric = ''.join([str.lower(letter) for letter in s if letter in dictionary])
        return alphanumeric[::-1] == alphanumeric
        


s = Solution()
print s.isPalindrome("A man, a plan, a canal: Panama")
print s.isPalindrome("asdfjiejfwe awefawe.a wef.aw.efa .")
