#!/usr/bin/python

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate(self, nums, k):
        nums = nums[k+1:] + nums[:k+1]
