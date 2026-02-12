# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        preOrderNodes = []
        def traversePreOrder(root):
            if root:
                preOrderNodes.append(root)
                traversePreOrder(root.left)
                traversePreOrder(root.right)
            
        traversePreOrder(root)
        n = len(preOrderNodes)

        for idx, node in enumerate(preOrderNodes[:n - 1]):
            node.left = None
            node.right = preOrderNodes[idx + 1]

        