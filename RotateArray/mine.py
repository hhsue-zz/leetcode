#!/usr/bin/python

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate(self, nums, k):
        l = range(1,nums+1)
        return l[k+1:] + l[:k+1]

    
s = Solution()
print s.rotate(2,1)
