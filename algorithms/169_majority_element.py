class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        majority_element = nums[0]
        count = 1

        for i, ele in enumerate(nums[1:]):
            print i, ele
            if count == 0:
                count += 1
                majority_element = nums[i + 1]
            elif majority_element == nums[i + 1]:
                count += 1
            else:
                count -= 1

        return majority_element

sol = Solution()
print sol.majorityElement([6, 5, 5])