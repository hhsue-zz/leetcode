MAXINT=2**31
class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        if x > MAXINT:
            return 0
        my_str = str(x)
        negative = False
        if my_str[0] == '-':
            my_str = my_str[1:]
            negative = True
        rev_str = my_str[::-1]
        if negative:
            output = '-' + str(rev_str)
        else:
            output = str(rev_str)
        output = int(output)
        if output > MAXINT:
            return 0
        else:
            return output

s = Solution()
print s.reverse(1)
