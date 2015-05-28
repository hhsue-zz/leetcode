#!/usr/bin/python


class Solution:
# @param a list of integers
# @return an integer

    def removeDuplicates(self, A):
        if not A:
            return 0
        else:
            ii,jj=1,1
            while jj<len(A):
                if A[ii-1]!=A[jj]:
                    A[ii]=A[jj]
                    ii+=1
                jj+=1
            return ii


s = Solution()
print s.removeDuplicates([1,1,2,1,1])

