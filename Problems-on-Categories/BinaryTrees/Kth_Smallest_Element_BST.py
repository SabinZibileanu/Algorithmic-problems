class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # in order traversal O(n)
        
        treeNodes = []
        def inOrderTraversal(root):
            if root:
                inOrderTraversal(root.left)
                treeNodes.append(root.val)
                inOrderTraversal(root.right)
        
        inOrderTraversal(root)
        return treeNodes[k - 1]
    

class Solution2:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # level order traversal + sort O(nlogn)
        
        treeNodes = [root.val]
        currLevel = [root]
        while currLevel:
            nextLevel = []
            for node in currLevel:
                if node.left:
                    treeNodes.append(node.left.val)
                    nextLevel.append(node.left)
                
                if node.right:
                    treeNodes.append(node.right.val)
                    nextLevel.append(node.right)
            
            currLevel = nextLevel
        
        return sorted(treeNodes)[k - 1]