#!/usr/bin/python
import collections

class Solution:
# @param {string} s
# @param {string} t
# @return {string}
# sliding window problem
# count all chars in string T
# left pointer point to string which has been processed
# right pointer point to string, which has not been processed
# 1.if all window from left to right contains all string T(counter values all less then or equal to 0)
#   calculate min window length, and keep answer
#   then move left pointer
# 2.else there are missing string in current answer
#   move right pointer
#   update counter
# repeat 1, 2 steps until right is equal to len(s), then break it
    def minWindow(self, s, t):
        left, right = 0, 0
        # count T chars
        counter = collections.defaultdict(int)
        for a in t:
            counter[a] += 1

        minwindow = len(s) + 1
        answer = None

        while right <= len(s):
            # check all chars in T are in the current answer
            if all(map(lambda x: True if x<=0 else False, counter.values())):
                if minwindow > right-left:
                    minwindow = right-left
                    answer = s[left:right]
                    print answer
                char = s[left]
                if char in counter:
                    counter[char] += 1
                left += 1
            else:
                if right == len(s):
                    break
                char = s[right]
                if char in counter:
                    counter[char] -= 1
                right += 1

        return answer if answer else ''


s = 'ADOBECODEBANC'
t = 'ABC'
sol = Solution()
print sol.minWindow(s,t)
