# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.is_mirror(root, root)

    def is_mirror(self, p, q):
        if not p and not q:
            return True
        if (not p and q) or (not q and p):
            return False

        return self.is_mirror(p.left, q.right) and self.is_mirror(p.right, q.left) and p.val == q.val
