# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return None

        dummy_node = ListNode(0)
        curr_node = dummy_node
        leading = 0
        while l1 and l2:
            curr_val = l1.val + l2.val + leading
            if curr_val >= 10:
                curr_val -= 10
                leading = 1
            else:
                leading = 0
            curr_node.next = ListNode(curr_val)
            curr_node = curr_node.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            curr_val = l1.val + leading
            if curr_val >= 10:
                curr_val -= 10
                leading = 1
            else:
                leading = 0
            curr_node.next = ListNode(curr_val)
            curr_node = curr_node.next
            l1 = l1.next

        while l2:
            curr_val = l2.val + leading
            if curr_val >= 10:
                curr_val -= 10
                leading = 1
            else:
                leading = 0
            curr_node.next = ListNode(curr_val)
            curr_node = curr_node.next
            l2 = l2.next

        if leading:
            curr_val = leading
            leading = 0
            curr_node.next = ListNode(curr_val)
            curr_node = curr_node.next

        curr_node.next = None
        return dummy_node.next
