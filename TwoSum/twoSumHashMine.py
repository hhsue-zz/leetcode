#!/usr/bin/python

# first value smaller
# non-zero indexing
# account for multiple possibilities

class Solution:
    def twoSum(self, num, target):
        results = []
        for i in range(len(num)):
            diff = target - num[i]
            if diff in num:
                if num[i] < diff:
                    results.append((i+1, num.index(diff)+1))
                else: 
                    results.append((num.index(diff)+1, i+1))
        return set(results)
'''
class Solution2:
    def twoSum(self, num, target):
        compl = {}
        results = []
        for i in range(len(num)):
            if num[i] not in compl:
                compl[target-num[i]] = i
            else:
                if num[i] < target-num[i]:
                    results.append((i+1,compl[num[i]]+1))
                else:
                    results.append((compl[num[i]]+1,i+1))
        return results
'''        
    
s=Solution()
#print s.twoSum([12,2,7,11,15,14],24)
print s.twoSum([3,2,4,5,2,3,7,9,3,5,4,2,6,7,23,3,2,100],123)

# find num[i], such that num[j]
# target = num[i] + num[j]
# target - num[i] = num[j]
# target - num[j] = num[i]
# 9,13,17,18,22,26
# 24,19,15,11

