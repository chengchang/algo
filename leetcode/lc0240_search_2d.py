# coding: utf-8
# from: https://leetcode-cn.com/problems/search-a-2d-matrix-ii/
# keys: arr-2d


from typing import List


def search_2d(matrix: List[List[int]],
              target: int) -> bool:
    m, n = len(matrix), len(matrix[0])
    i, j = 0, m - 1
    while i < n and j >= 0:
        cur = matrix[i][j]
        if cur < target:
            i += 1
        elif cur > target:
            j -= 1
        else:
            return True
    return False


if __name__ == '__main__':
    mat = [[1, 4, 7, 11, 15],
           [2, 5, 8, 12, 19],
           [3, 6, 9, 16, 22],
           [10, 13, 14, 17, 24],
           [18, 21, 23, 26, 30]]

    assert search_2d(mat, 5) is True
    assert search_2d(mat, 19) is True
    assert search_2d(mat, 20) is False
