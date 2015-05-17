import math

class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        composites = {}
        limit = int(math.ceil(math.sqrt(n)))
        for i in range(2,limit):
            if i not in composites:
                for j in range(i+1,n):
                    if j not in composites:
                        if j%i == 0:
                            composites[j] = 1
                        else:
                            pass
        return n - len(composites)


s = Solution()
print s.countPrimes(999983)
