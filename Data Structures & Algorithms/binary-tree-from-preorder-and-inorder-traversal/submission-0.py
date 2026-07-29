# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
    I use preorder to identify the root, 
    because the root is always first there. 
    Then I use inorder to split the remaining nodes 
    into the left and right subtrees. 
    Once I know the left subtree size, 
    I can split preorder accordingly and recursively build both sides.
"""
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder :
            return None
        root = TreeNode(preorder.pop(0))
        rootInorderIndex = 0
        for i in range(len(inorder)):
            if inorder[i] == root.val:
                rootInorderIndex = i
                break
        leftpreorder,rightpreorder = preorder[:rootInorderIndex],preorder[rootInorderIndex:]
        leftinorder,rightinorder = inorder[:rootInorderIndex], inorder[rootInorderIndex+1:]
        root.left = self.buildTree(leftpreorder,leftinorder)
        root.right = self.buildTree(rightpreorder,rightinorder)
        return root






