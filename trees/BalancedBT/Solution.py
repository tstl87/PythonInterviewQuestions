class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def helper(root):
            if not root:
                return (True,0)
            else:
                leftb, lefth = helper(root.left)
                rightb, righth = helper(root.right)
            return (leftb and rightb and abs(lefth - righth) <= 1, max(lefth, righth) + 1)
        return helper(root)[0]
    
# Time complexity: O(n)
# Since we traverse through the tree once

# Space complexity: O(n)
# recursive stack.