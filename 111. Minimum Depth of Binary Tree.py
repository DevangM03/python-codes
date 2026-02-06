# definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root):
        # if tree is empty
        if root is None:
            return 0
        
        # if left child is missing, go right
        if root.left is None:
            return 1 + self.minDepth(root.right)
        
        # if right child is missing, go left
        if root.right is None:
            return 1 + self.minDepth(root.left)
        
        # if both children exist, take the minimum
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

root = TreeNode(3)
#root.left = TreeNode(9)
#root.right = TreeNode(20)
#root.right.left = TreeNode(15)
#root.right.right = TreeNode(7)

sol = Solution()
print(sol.minDepth(root))
