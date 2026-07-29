# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def minTreeNode(root):
    if not root:
        return None
    if root.left and root.right :
        return min(root.val,minTreeNode(root.left),minTreeNode(root.right))
    elif root.left and not root.right : 
        return min(root.val,minTreeNode(root.left))
    elif not root.left and root.right:
        return min(root.val,minTreeNode(root.right))
    return root.val

def maxTreeNode(root):
    if not root:
        return None
    if root.left and root.right :
        return max(root.val,maxTreeNode(root.left),maxTreeNode(root.right))
    elif root.left and not root.right : 
        return max(root.val,maxTreeNode(root.left))
    elif not root.left and root.right:
        return max(root.val,maxTreeNode(root.right))
    return root.val


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        isValidRight = True if (not root.right or (minTreeNode(root.right) > root.val)) else False
        isValidLeft = True if (not root.left or (maxTreeNode(root.left) < root.val)) else False
        isValid = isValidLeft and isValidRight
        return isValid and self.isValidBST(root.left) and self.isValidBST(root.right)


