# Maximum Binary Tree
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        if nums == []:
            return None
        node, idx = TreeNode(max(nums)), nums.index(max(nums))            
        node.left = self.constructMaximumBinaryTree(nums[:idx])
        node.right = self.constructMaximumBinaryTree(nums[idx + 1:])            
        return node