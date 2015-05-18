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
        for letter in s:
            if letter in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ':
                words_only += str.lower(letter)
        truncated_string = ''.join([words.strip() for words in words_only.split()])
        reversed_string = truncated_string[::-1]
        if reversed_string == truncated_string:
            return True
        else:
            return False
        


s = Solution()
print s.isPalindrome("A man, a plan, a canal: Panama")
print s.isPalindrome("asdfjiejfwe awefawe.a wef.aw.efa .")
