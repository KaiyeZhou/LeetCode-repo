# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind+1:])
            return root
        # 22
        # 先序遍历的列表为[根，左，右]，中序遍历的列表为[左，根，右]，则中序遍历中根的下标为先序遍历中左的边界
        if inorder==[]:
            return None
        root = TreeNode(preorder[0])
        #print(preorder,inorder)
        x = inorder.index(root.val)#找到根在中序中的位置
        root.left=self.buildTree(preorder[1:x+1],inorder[0:x])
        root.right=self.buildTree(preorder[x+1:],inorder[x+1:])
        return root
        
        # 迭代
        if not preorder or not inorder:
            return
        root = TreeNode(preorder[0])
        stack = [root]
        i = 0
        
        for node in preorder[1:]:
            parent = stack[-1]
            
            if parent.val != inorder[i]:
                parent.left = TreeNode(node)
                stack.append(parent.left)
            else:
                while stack and stack[-1].val == inorder[i]:
                    parent = stack.pop()
                    i += 1
                parent.right = TreeNode(node)
                stack.append(parent.right)
        return root