# Reverse Integer
class Solution(object):
    def reverse(self, x):
        if x < 0:
            sign = -1
        else:
            sign = 1

        x = str(abs(x))[::-1]
        rev = int(x) * sign
        if -2**31 <= rev <= 2**31 -1:
            return rev
        else:
            return 0