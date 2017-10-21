class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x == None:
            return False

        if x < 0:
            return False

        if x != 0 and x % 10 == 0:
            return False

        rev = 0
        while x > rev:
            rev = rev * 10 + x % 10
            x = x / 10

        return x == rev or x == rev / 10
