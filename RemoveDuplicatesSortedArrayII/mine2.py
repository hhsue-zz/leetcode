'''
[1,1,1,2,2,3]
[1,1,2,2,3],3]  -> compare index with modified_length (cumulative)
'''

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        if len(nums) <= 1:
             return len(nums)
        i = 1 # index to compare with
        j = 0 #
        d = 0 # duplicates
        count = 0
        while i < len(nums):
            if nums[i] != nums[j]:
                d = 0
                j += 1
            else:
                d += 1
                if d > 1:
                    pass
                else:
                    j += 1
            nums[j] = nums[i]
            i += 1
        count = j + 1
        print nums[:count]
        return count

s = Solution()
print s.removeDuplicates([1,1,1,1,2,2,3])
#print s.removeDuplicates([1,1,1])


