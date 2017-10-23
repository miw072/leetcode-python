class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        curr_sum = max_sum = nums[0]
        for ele in nums[1:]:
            curr_sum = max(ele, curr_sum + ele)
            max_sum = max(max_sum, curr_sum)

        return max_sum
