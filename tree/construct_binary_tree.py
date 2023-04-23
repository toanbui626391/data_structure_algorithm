"""
strategy to solve the problem:
    problem: construct binary tree with preorder and inorder
    why:
        the first element of preorder is root
        the index of the root in inorder will divide left subTree and right subTree of the current node
        relation between mid, preorder, inorder
            mid + preorder: to find direct left and right node of the current root.
            mid + inorder: to find nodes in left subTree and right subTree
        
        to build binary search tree we need to know
            currentt node: first element of preorder
            left and right tree: 
                left: inorder[:mid]
                right: inorder[mid+1:]
            find current node:
                left: preorder[1:mid+1]
                right: preorder[mid+1:]
    variables:
        root (TreeNode): to find the current node
        mid (int): to help find preorder and inorder for next recursive

    notes:
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

    

"""
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #base case
        if not preorder or not inorder:
            return None
        #init root and mid
        root = TreeNode(preorder[0]) #root have to be TreeNode
        mid = inorder.index(preorder[0])
        #find left and right node of the current node
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid]) #remove the curretn root in preorder and reduce search range for left
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
        return root