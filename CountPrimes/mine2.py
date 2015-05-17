#!/usr/bin/python

import math

class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        composites = {}
        limit = int(math.ceil(math.sqrt(n)))
        for i in range(2,limit):
            multiple = 0
            while True:
                multiple += 1
                value = multiple * i
                if value > n:
                    break
                else:
                    composites[multiple * i] = 1 
        return n - len(composites) 

s=Solution()
print s.countPrimes(999983)


                 
