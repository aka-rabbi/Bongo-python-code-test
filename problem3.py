def lca(root, node1, node2):
    if root is None:
        return None

    if root.val == node1 or root.val == node2:
        return root

    left_result = lca(root.left, node1, node2)
    right_result = lca(root.right, node1, node2)

    if left_result and right_result:
        return root

    return left_result if left_result is not None else right_result