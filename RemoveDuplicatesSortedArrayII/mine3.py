'''
[1,1,1,2,2,3]
[1,1,2,2,3],3]  -> compare index with modified_length (cumulative)
'''

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        current = None
        count = 1
        cumulative = 0
        for i in range(len(nums)):
            if nums[i] != current:
                count = 1
                current = nums[i]
                nums[cumulative] = nums[i]
                cumulative += 1
            else:
                count += 1
                if count < 3:
                    nums[cumulative] = nums[i]
                    cumulative += 1
                else:
                    pass
        print nums[:cumulative]
        return cumulative


                


s = Solution()
print s.removeDuplicates([1,1,1,1,2,2,3])
print s.removeDuplicates([1,1,1,1,1])
#print s.removeDuplicates([1,1,1])


