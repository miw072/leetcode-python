class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_mapping = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }
        ret = 0
        for i in range(0, len(s) - 1):
            if roman_mapping[s[i]] < roman_mapping[s[i + 1]]:
                ret -= roman_mapping[s[i]]
            else:
                ret += roman_mapping[s[i]]

        return ret + roman_mapping[s[-1]]
