def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    result = []
    if root:
        result.append(root.val)
        result.extend(self.preorderTraversal(root.left))
        result.extend(self.preorderTraversal(root.right))
    return result