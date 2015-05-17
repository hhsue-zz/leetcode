class Solution:
# @param {integer} n
# @return {integer}
    def countPrimes(self, n):
        if n < 3:
            return 0
        #primes = [True] * n
        primes = {}
        primes[0] = primes[1] = False
        for i in xrange(2, n):
            primes[i] = True
        for i in xrange(2, int(n ** 0.5) + 1):
            if primes[i]:
                for x in xrange(i * i, n, i):
                    primes[x] = False
                #The following can replace the for loop above, which halves the calculation time
                #primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
        return sum(primes.itervalues())


s = Solution()
print s.countPrimes(999983)



