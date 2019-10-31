# coding: utf-8


# from: https://leetcode-cn.com/problems/4sum/
# keys: n_sum, ij

from typing import List


# Time: O(n^4), Space: O(1)
def four_sum(arr: List[int], target: int) \
        -> List[List[int]]:
    if not arr:
        return []

    ret = []
    p = len(arr) - 1
    while p >= 3:
        k = p - 1
        while k >= 2:
            j = k - 1
            while j >= 1:
                for i in range(j):
                    cur = [arr[i], arr[j],
                           arr[k], arr[p]]
                    if target == sum(cur):
                        ret.append(cur)
                j -= 1
            k -= 1
        p -= 1

    return ret


# Time: O(n^3), Space: O(1)
def four_sum_ij(arr: List[int], target: int) \
        -> List[List[int]]:
    if not arr:
        return []

    arr.sort()

    ret = []
    p = len(arr) - 1
    while p >= 3:
        new_t = target - arr[p]
        k = p - 1
        # 转化为3数和
        while k >= 2:
            i, j = 0, k - 1
            nk = arr[k]
            while i < j:
                ni, nj = arr[i], arr[j]
                cur = ni + nj + nk
                if new_t == cur:
                    ret.append([arr[p], nk, nj, ni])

                    # 同值跳
                    while i < j and arr[i + 1] == ni:
                        i += 1
                    while i < j and arr[j - 1] == nj:
                        j -= 1
                    i += 1
                    j -= 1
                elif new_t > cur:
                    i += 1
                else:
                    j -= 1

            # 同值跳
            while k >= 2 and arr[k - 1] == arr[k]:
                k -= 1
            k -= 1

        # 同值跳
        while p >= 2 and arr[p - 1] == arr[p]:
            p -= 1
        p -= 1

    return ret


if __name__ == '__main__':
    fn1, fn2 = four_sum, four_sum_ij
    true = [[2, 1, -1, -2], [2, 0, 0, -2], [1, 0, 0, -1]]
    assert fn1([1, 0, -1, 0, -2, 2], 0) == true
    assert fn2([1, 0, -1, 0, -2, 2], 0) == true
