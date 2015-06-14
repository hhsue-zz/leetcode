#!/usr/bin/python

#[0,1,2,3,4,5,6]
#[4,5,6,0,1,2,3]

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead. 
    def rotate(self, nums, k):
        mod = k % len(nums)
        d = {} #{index:value}
        for i in range(0,len(nums)):
            if i < len(nums) - mod - 1:
                d[nums[i+mod]] = i 
                if i in d:
                    nums[i+mod] = d[i]
                else:
                    nums[i+mod] = nums[i] 
            else:
                if i in d:
                    new_index = i + mod - len(nums)
                    nums[new_index] = d[i]
        return nums

 
s = Solution()
print s.rotate([0,1,2,3,4,5,6], 3) 
