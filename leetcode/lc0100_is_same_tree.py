# coding: utf-8
# from: https://leetcode-cn.com/problems/search-a-2d-matrix-ii/
# keys: arr-2d

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def is_same_tree(p: TreeNode,
                 q: TreeNode) -> bool:
    if p is None and q is None:
        return True

    if p is None or q is None:
        return False

    return p.val == q.val and \
        is_same_tree(p.left, q.left) and \
        is_same_tree(p.right, q.right)


def is_same_tree2(p: TreeNode,
                  q: TreeNode) -> bool:
    s = list()
    s.append(p)
    s.append(q)

    while s:
        x = s.pop()
        y = s.pop()
        if x is None and y is None:
            continue

        if x is None or y is None:
            return False

        if x.val != y.val:
            return False

        s.append(x.left)
        s.append(y.left)
        s.append(x.right)
        s.append(y.right)

    return True


def create_t(arr, root, i=0, n=-1):
    if n < 0:
        n = len(arr)

    if i < n:
        root = TreeNode(arr[i])
        root.left = create_t(arr, root.left, 2 * i + 1, n)
        root.right = create_t(arr, root.right, 2 * i + 2, n)

    return root


if __name__ == '__main__':
    arr = [1, 2, 2, 3, 4, 4, 3]
    arr2 = [1, 2, 2, 3, 4, 4]
    p = q = None
    p = create_t(arr, p)
    q = create_t(arr2, q)

    assert is_same_tree(p, q) == False
    assert is_same_tree(p, p) == True
