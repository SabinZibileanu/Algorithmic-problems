class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Brute force (n ^ 2)
        def rightDFS(rootNode, rootVal):
            if rootNode.val <= rootVal:
                return False
            currLevel = [rootNode]
            
            while currLevel:
                nextLevel = []
                for node in currLevel:
                    if node.left:
                        if node.left.val <= rootVal or node.left.val >= node.val:
                            return False
                        nextLevel.append(node.left)
                    
                    if node.right:
                        if node.right.val <= rootVal or node.right.val <= node.val:
                            return False
                        nextLevel.append(node.right)
                
                currLevel = nextLevel

            if rootNode.left:
                if not leftDFS(rootNode.left, rootNode.val):
                    return False
            
            if rootNode.right:
                if not rightDFS(rootNode.right, rootNode.val):
                    return False
            
            return True
        
        def leftDFS(rootNode, rootVal):
            if rootNode.val >= rootVal:
                return False
            currLevel = [rootNode]
            
            while currLevel:
                nextLevel = []
                for node in currLevel:
                    if node.left:
                        if node.left.val >= rootVal or node.left.val >= node.val:
                            return False
                        nextLevel.append(node.left)
                        
                    if node.right:
                        if node.right.val >= rootVal or node.right.val <= node.val:
                            return False
                        nextLevel.append(node.right)
                
                currLevel = nextLevel

            if rootNode.left:
                if not leftDFS(rootNode.left, rootNode.val):
                    return False
            
            if rootNode.right:
                if not rightDFS(rootNode.right, rootNode.val):
                    return False
            
            return True
        
        if not root: return True
        leftValid = rightValid = True

        if root.left:
            leftValid = leftDFS(root.left, root.val)
        
        if root.right:
            rightValid = rightDFS(root.right, root.val)
        
        return leftValid and rightValid

class Solution2:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Recursive O(n)
        def isValidSubTree(node, left, right):
            if not node:
                return True
            
            if not (node.val < right and node.val > left):
                return False
            
            return isValidSubTree(node.left, left, node.val) and isValidSubTree(node.right, node.val, right)

        isValidSubTree(root, float('-inf'), float('inf'))