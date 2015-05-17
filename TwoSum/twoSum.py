#!/usr/bin/python

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]
                
s = Solution()
print s.twoSum([3,2,4,5,2,3,7,9,3,5,4,2,6,7,23,3,2,100],123)            
