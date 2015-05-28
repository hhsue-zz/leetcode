#!/usr/bin/python

# 1. every open bracket must be closed
# 2. must open bracket before closing
# 3. cannot interleave brackets (cannot open bracket then immediately close a different type bracket)
# keep track of brackets opened and not closed via dictionary values
# if a bracket's value is less than 0, then we've closed more than opened
# if bracket is positive, before program closes, then we've not closed a bracket
# current_open_bracket will keep track of the current open bracket. 

class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, my_str):
        brackets_unclosed = {}
        close_bracket = {'{':'}','[':']','(':')',None:None}
        open_bracket = {'}':'{',']':'[',')':'(',None:None}
        current_open_bracket = None
        previous_open_bracket = None
        for s in my_str: 
            if s in '{[(':
                if s in brackets_unclosed:
                    brackets_unclosed[s] += 1
                else:
                    brackets_unclosed[s] = 1
                previous_open_bracket = current_open_bracket
                current_open_bracket = s
            elif s in '}])':
                if open_bracket[s] not in brackets_unclosed:
                    return False
                elif s in brackets_unclosed and brackets_unclosed[s] <= 0:
                    return False
                elif s != close_bracket[current_open_bracket]:
                    # if current open bracket is None, then False. 
                    return False
                else:
                    brackets_unclosed[open_bracket[s]] -= 1
                    current_open_bracket = previous_open_bracket
                    print current_open_bracket
            else:
                pass
        for v in brackets_unclosed.itervalues():
            if v > 0:
                return False
        return True

my_input = '[{{{([][])}}[]}'
my_input2 = ']'
my_input3 = '{'
my_input4 = '))'
s = Solution()
print s.isValid(my_input)
print s.isValid(my_input2)
print s.isValid(my_input3)
print s.isValid(my_input4)
