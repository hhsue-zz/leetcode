#!/usr/bin/python

class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        #dictionary O(n)
        dict = {}
        for i in range(len(num)):
            # check if num[index], or value is a key to dict
            if num[i] not in dict:
                dict[target-num[i]] = i
            else:
                return (dict[num[i]]+1, i+1)
        return (-1, -1)

s=Solution()
#print s.twoSum([2,7,11,15],13)
print s.twoSum([3,2,4,5,2,3,7,9,3,5,4,2,6,7,23,3,2,100],123)

# check if 2 in dict
# add 11:0 to dict
# check if 7 in dict
# no, add 6:1 to dict
# check if 11 in dict
# yes, return 0+1,2+1 = 1,3 

# store the complement if num[i]
# {11,6,2,-}
# dict[target-num[i]]=i
# target = num[i] + num[j]

# find i and j
