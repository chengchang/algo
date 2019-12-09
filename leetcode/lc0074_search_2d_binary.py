# coding: utf-8
# from: https://leetcode-cn.com/problems/search-a-2d-matrix-ii/
# keys: arr-2d
from typing import List


def search_2d_binary(matrix: List[List[int]], target: int) -> bool:

    if not matrix:
        return False

    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1

    def get_pos(x):
        i = x // n
        j = x % n
        return i, j

    while left <= right:
        mid = (left + right) // 2
        i, j = get_pos(mid)
        if target < matrix[i][j]:
            right = mid - 1
        elif target > matrix[i][j]:
            left = mid + 1
        else:
            return True

    return False



if __name__ == '__main__':
    mat = [[1, 3, 5, 7],
           [10, 11, 16, 20],
           [23, 30, 34, 50]]

    assert search_2d_binary(mat, 3) is True
    assert search_2d_binary(mat, 13) is False
