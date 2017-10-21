# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return None
        if not l1:
            return l2
        if not l2:
            return l1

        dummy_node = ListNode(0)
        curr_node = dummy_node
        while l1 and l2:
            if l1.val <= l2.val:
                new_val = l1.val
                l1 = l1.next
            else:
                new_val = l2.val
                l2 = l2.next
            curr_node.next = ListNode(new_val)
            curr_node = curr_node.next

        if l1:
            curr_node.next = l1
        if l2:
            curr_node.next = l2

        return dummy_node.next
