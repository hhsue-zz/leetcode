#!/usr/bin/python

class Solution:
    # @param {integer} x
    # @return {integer}
    def mySqrt(self, x):
        if x == 1:
            return 1
        b = x
        a = 0
        while True:
            z = int((a + b) / 2)
            attempt = z * z
            if b - a == 1:
                return -1
            if attempt > x:
                b = z
            elif attempt < x:
                a = z
            else:
                return z 
s = Solution()

print s.mySqrt(101)
