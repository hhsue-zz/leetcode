#!/usr/bin/python

# not zero based 
# negative integers? 
# format of output? 
# integer overflow 
# test for real integers 
# order of integers given 
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        complementIndex = {}
        for i in range(len(nums)):
            complement = target-nums[i]
            if complement in complementIndex:
                return complementIndex[complement] + 1, i + 1
            else:
                complementIndex[nums[i]] = i
        return -1, -1

s = Solution()
print s.twoSum([2,7,11,15],26)


