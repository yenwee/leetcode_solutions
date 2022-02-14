# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.recurse(root, 1) if root != None else 0
    
    def recurse(self, root: Optional[TreeNode], curr):
        ans = 0
        if not root.right and not root.left: 
            return curr
        
        if root.left:
            ans = max(ans, self.recurse(root.left, curr + 1))
            
        if root.right:
            ans = max(ans, self.recurse(root.right, curr + 1))
            
        return ans