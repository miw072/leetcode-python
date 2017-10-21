import math


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == None:
            return None

        if x < 0:
            sign = -1
            x = -x
        else:
            sign = 1

        reversed_digits = []
        while x > 0:
            reversed_digits.append(str(x % 10))
            x = x / 10

        if not reversed_digits:
            return 0

        cap_int = int(math.pow(2, 31) - 1)
        rst = int(''.join(reversed_digits))
        if rst > cap_int:
            return 0

        return sign * rst
