# Invert Binary Tree : O(n)
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        
        r, l = self.invertTree(root.right), self.invertTree(root.left)
        
        root.right = l
        root.left = r
                
        return root