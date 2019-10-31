# coding: utf-8

# from: https://leetcode-cn.com/problems/3sum/
# keys: n_sum, ij

from typing import List


# Time: O(n^2), Space: O(1)
def three_sum_ij(arr: List[int]) -> List[List[int]]:
    if not arr:
        return []

    arr.sort()

    ret = []
    k = len(arr) - 1
    while k >= 2:
        # 早停
        if arr[k] < 0:
            break

        i, j = 0, k - 1
        while i < j:
            cur = arr[i] + arr[j] + arr[k]

            if cur == 0:
                ret.append([arr[i], arr[j], arr[k]])
                # 同值跳
                while i < j and arr[i + 1] == arr[i]:
                    i += 1
                # 同值跳
                while i < j and arr[j - 1] == arr[j]:
                    j -= 1
                i += 1
                j -= 1
            elif cur > 0:
                j -= 1
            else:
                i += 1

        # 同值跳
        while k >= 2 and arr[k - 1] == arr[k]:  # move
            k -= 1
        k -= 1
    return ret


if __name__ == '__main__':
    r = three_sum_ij([-1, 0, 1, 2, -1, -4])
    assert r == [[-1, -1, 2], [-1, 0, 1]]
