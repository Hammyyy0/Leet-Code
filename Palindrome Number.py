# Palindrome Number
class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        return str(x) == x[::-1]
    