class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) < 2:
            return len(nums)

        ret = 0
        for i, ele in enumerate(nums[1:]):
            if ele != nums[ret]:
                ret += 1
                nums[ret] = ele

        return ret + 1
