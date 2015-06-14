class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        current = None
        cumulative = 0
        count = 0
        for i in xrange(len(nums)):
            if current != nums[cumulative]:
                current = nums[cumulative]
                count = 1
                cumulative += 1
            else:
                count += 1
                if count > 2:
                    nums.pop(cumulative)
                    continue
                else:
                    cumulative += 1
        print nums[:cumulative]
        return cumulative 
                

s = Solution()
print s.removeDuplicates([1,1,1,2,2,3])

