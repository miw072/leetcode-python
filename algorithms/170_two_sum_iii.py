class TwoSum(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.elements = []

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        if number == None:
            return
        self.elements.append(number)

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        if not self.elements or value == None:
            return False
        helper_dict = {}
        for i, ele in enumerate(self.elements):
            complement = value - ele
            if complement in helper_dict:
                return True
            helper_dict[ele] = i
        return False



# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)