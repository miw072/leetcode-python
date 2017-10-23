class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits == None:
            return None

        curr_digit = digits[-1]
        curr_index = len(digits) - 1
        while curr_digit == 9:
            digits[curr_index] = 0
            if curr_index == 0:
                digits.insert(0, 1)
                return digits
            curr_digit = digits[curr_index - 1]
            curr_index = curr_index - 1

        digits[curr_index] = digits[curr_index] + 1
        return digits
