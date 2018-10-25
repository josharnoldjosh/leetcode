# Merge Two Binary Trees
class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1 and not t2:
            return None
        
        result = TreeNode((t1.val if t1 else 0) + (t2.val if t2 else 0))
        
        result.left = self.mergeTrees(t1 and t1.left, t2 and t2.left)
        result.right = self.mergeTrees(t1 and t1.right, t2 and t2.right)
        
        return result