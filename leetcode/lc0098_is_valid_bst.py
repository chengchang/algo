# coding: utf-8
# from: https://leetcode-cn.com/problems/validate-binary-search-tree/
# keys: bst, recursion

from typing import Union

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def bst_min(root: TreeNode) -> TreeNode:
    while root.left is not None:
        root = root.left
    return root


def bst_max(root: TreeNode) -> TreeNode:
    while root.right is not None:
        root = root.right
    return root


def is_valid_bst(root: TreeNode) -> bool:
    if root is None:
        return True

    is_valid_left = root.left is None or \
        root.val > bst_max(root.left).val
    is_valid_right = root.right is None or \
        root.val < bst_min(root.right).val

    return is_valid_left and \
        is_valid_right and \
        is_valid_bst(root.left) and \
        is_valid_bst(root.right)


def _is_valid_bst_bound(root: TreeNode,
                        high: Union[TreeNode, None],
                        low: Union[TreeNode, None]) -> bool:
    if root is None:
        return True

    if low is not None and root.val >= low.val:
        return False
    if high is not None and root.val <= high.val:
        return False

    return _is_valid_bst_bound(root.left, low, root) and \
        _is_valid_bst_bound(root.right, root, high)


def is_valid_bst_bound(root: TreeNode) -> bool:
    return _is_valid_bst_bound(root, None, None)


def create_level_order(arr, root, i, n):
    if i < n:
        root = TreeNode(arr[i])
        root.left = create_level_order(arr, root.left, 2 * i + 1, n)
        root.right = create_level_order(arr, root.right, 2 * i + 2, n)

    return root


if __name__ == '__main__':
    arr = [2, 1, 3]
    root = None
    root = create_level_order(arr, root, 0, len(arr))
    assert is_valid_bst(root)
    assert is_valid_bst_bound(root)
