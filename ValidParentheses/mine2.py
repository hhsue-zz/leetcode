#!/usr/bin/python

# 1. every open bracket must be closed
# 2. must open bracket before closing
# 3. cannot interleave brackets (cannot open bracket then immediately close a different type bracket)
# keep a stack of open brackets, that is emptied as brackets close. stack must be empty at the end. 
# top bracket must be closed by corresponding closing bracket

class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, my_str):
        stack = []
        open_bracket = {'}':'{',']':'[',')':'('}
        for s in my_str:
            if s in '[{(':
                stack.append(s)
            elif s in ']})':
                if stack and stack[-1] == open_bracket[s]:
                    stack.pop()
                else:
                    return False
            else:
                pass
        if stack:
            return False
        return True


my_input = '[]'
my_input2 = '[[[]]]()()[234]{([[3]4(2)3])}'
my_input3 = '{'
my_input4 = '))'
s = Solution()
print s.isValid(my_input)
print s.isValid(my_input2)
print s.isValid(my_input3)
print s.isValid(my_input4)
