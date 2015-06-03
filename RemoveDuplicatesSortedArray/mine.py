#!/usr/bin/python

class solution:
# @param a list of integers
# @return an integer
    def removeDuplicates(self, A):
        pointer = 0
        result = 1
        length = len(A)
        if not A:
            return 0
        while pointer < length - 1:
            if A[pointer] != A[pointer+1]:
                A[result] = A[pointer+1]
                result += 1
            pointer += 1
        return result

s = solution()
print s.removeDuplicates([1,2,3,3])
