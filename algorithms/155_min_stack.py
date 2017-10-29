class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.normal_stack = []
        self.min_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if x == None:
            return
        self.normal_stack.append(x)
        curr_min = self.getMin()
        if curr_min == None or x <= curr_min:
            self.min_stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if self.normal_stack:
            if self.normal_stack[-1] == self.getMin(): self.min_stack.pop()
            self.normal_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if not self.normal_stack:
            return None
        return self.normal_stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if self.min_stack:
            return self.min_stack[-1]

        return None

test_stack = MinStack()
test_stack.push(-2)
test_stack.push(0)
test_stack.push(-1)
print test_stack.getMin()
print test_stack.top()
test_stack.pop()
print test_stack.getMin()
