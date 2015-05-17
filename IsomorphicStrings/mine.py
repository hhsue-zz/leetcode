#!/usr/bin/python

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        mapping = {}
        # assume len(s) == len(t)
        # loop over s
        for i in range(len(s)):
            # if letter has not been mapped yet
            if s[i] not in mapping:
                # but we've already mapped to the next letter 
                if t[i] in mapping.values():
                    return False
                else:
                    mapping[s[i]] = t[i]
            # if letter has been mapped already
            else:
                # if existing map doesn't apply, return False
                if mapping[s[i]] != t[i]:
                    return False
        return True 

s = Solution()
print 'paper and title are', s.isIsomorphic('paper','title')
print 'babble and tippin are', s.isIsomorphic('babble','tippin')
print 'ab and aa are', s.isIsomorphic('ab','aa')
