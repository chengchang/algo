# coding: utf-8
# from: https://leetcode-cn.com/problems/symmetric-tree/
# keys: bst, recursion


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def _is_symmetric(s: TreeNode, t: TreeNode) -> bool:
    if s and t:
        return s.val == t.val and \
               _is_symmetric(s.left, t.right) and \
               _is_symmetric(s.right, t.left)
    else:
        return s is None and t is None


def is_symmetric_tree(root: TreeNode) -> bool:
    if not root:
        return True
    return _is_symmetric(root.left, root.right)


def is_symmetric_tree2(root: TreeNode) -> bool:
    if not root:
        return True

    stack = list()
    stack.append(root.left)
    stack.append(root.right)

    while len(stack) > 0:
        s = stack.pop()
        t = stack.pop()
        if s is None and t is None:
            continue
        if s is None or t is None:
            return False
        if s.val != t.val:
            return False

        stack.append(s.left)
        stack.append(t.right)
        stack.append(s.right)
        stack.append(t.left)

    return True


def create_level_order(arr, root, i, n):
    if i < n:
        root = TreeNode(arr[i])
        root.left = create_level_order(arr, root.left, 2 * i + 1, n)
        root.right = create_level_order(arr, root.right, 2 * i + 2, n)

    return root


def print_in_order(root):
    if root is not None:
        print_in_order(root.left)
        print(root.val, end=' ')
        print_in_order(root.right)


if __name__ == '__main__':
    arr = [1, 2, 2, 3, 4, 4, 3]

    root = None
    root = create_level_order(arr, root, 0, len(arr))
    # print_in_order(root)

    print(is_symmetric_tree(root))
    print(is_symmetric_tree2(root))
