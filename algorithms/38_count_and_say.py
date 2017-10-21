class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == None:
            return ''

        prev_count_say = '1'
        curr_count_say = prev_count_say
        for i in xrange(1, n):
            curr_count_say = ''
            curr_count = 1
            curr_say = prev_count_say[0]

            for j in xrange(1, len(prev_count_say)):
                if prev_count_say[j] != curr_say:
                    curr_count_say += str(curr_count)
                    curr_count_say += str(curr_say)
                    curr_count = 1
                    curr_say = prev_count_say[j]
                else:
                    curr_count += 1
            curr_count_say += str(curr_count)
            curr_count_say += str(curr_say)
            prev_count_say = curr_count_say

        return curr_count_say
