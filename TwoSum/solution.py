#!/usr/bin/python

class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        #dictionary O(n)
        dict = {}
        for i in range(len(num)):
            if num[i] not in dict:
                dict[target-num[i]] = i
            else:
                return (dict[num[i]]+1, i+1)
        return (-1, -1)

s = Solution()
print s.twoSum([3,2,4,5,2,3,7,9,3,5,4,2,6,7,23,3,2,100],123)
