#!/usr/bin/python

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        seenOnce = {}
        for n in nums:
            if n not in seenOnce:
                seenOnce[n] = 1
            else:
                del seenOnce[n]
        results = seenOnce.keys()
        if len(results) == 1:
            return results[0]

nums = [1,1,2,2,3]
s = Solution()
print s.singleNumber(nums) 
