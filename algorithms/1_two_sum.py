class Solution(object):
    # Solution 1
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums or target == None:
            return []
        helper_dict = {}
        for i, ele in enumerate(nums):
            complement = target - ele
            if complement in helper_dict:
                return [helper_dict.get(complement), i]
            helper_dict[ele] = i
        return []

    # Solution 2
    def twoSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums or target == None:
            return []

        for i, first_ele in enumerate(nums):
            for j, second_ele in enumerate(nums[(i + 1):]):
                if first_ele + second_ele == target:
                    return [i, j + i + 1]

        return []

