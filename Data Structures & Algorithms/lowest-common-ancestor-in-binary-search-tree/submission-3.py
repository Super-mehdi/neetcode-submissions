# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        stack = [root]
        while stack:
            candidate = stack[-1]
            if max(p.val,q.val)<candidate.val:
                stack.append(candidate.left)
            elif min(p.val,q.val)>candidate.val:
                stack.append(candidate.right)
            else:
                return candidate
        return None
        




