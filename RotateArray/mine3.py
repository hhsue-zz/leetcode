#!/usr/bin/python

#[0,1,2,3,4,5,6]
#[4,5,6,0,1,2,3]

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead. 
    def rotate(self, nums, k):
        mod = k % len(nums)
        if mod % 2 == 0:
            ###
        current_index = 0
        jump_index = None
        curr_pop = None
        prev_pop = nums[0]

        for i in range(len(nums)):
            if current_index + mod >= len(nums):
                jump_index = current_index + mod - len(nums)
            else:
                jump_index = current_index + mod
            print curr_pop
            curr_pop = nums[jump_index]
            nums[jump_index] = prev_pop
            prev_pop = curr_pop
            current_index = jump_index
        return nums
 
s = Solution()
print s.rotate([1,2,3,4,5,6], 2) 
