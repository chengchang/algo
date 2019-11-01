# coding: utf-8

# from: https://leetcode-cn.com/problems/find-in-mountain-array/
# keys: binary_search

from typing import List


def find_arr_mountain(arr: List[int],
                      target: int) -> int:
    if not arr:
        return -1

    size = len(arr) - 1
    left, right = 0, size

    while left < right:
        mid = (right + left) // 2

        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid

    if arr[left] == target:
        return left
    top = left

    left, right = 0, top
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid

    if arr[left] == target:
        return left

    left, right = top, size
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > target:
            left = mid + 1
        else:
            right = mid

    if arr[left] == target:
        return left

    return -1


def find_arr_mountain_opt(arr: List[int],
                          target: int) -> int:
    def bs(left, right, check_fn):
        while left < right:
            mid = (right + left) // 2
            if check_fn(mid):
                left = mid + 1
            else:
                right = mid
        return left

    if not arr:
        return -1

    n = len(arr) - 1
    pos = bs(0, n,
             lambda m: arr[m] < arr[m + 1])
    if arr[pos] == target:
        return pos

    top = pos
    pos = bs(0, top,
             lambda m: arr[m] < target)
    if arr[pos] == target:
        return pos

    pos = bs(top + 1, n,
             lambda m: arr[m] > target)
    if arr[pos] == target:
        return pos
    return -1


if __name__ == '__main__':
    c1, t1 = ([1, 2, 3, 4, 5, 3, 1], 3), 2
    c2, t2 = ([0, 1, 2, 4, 2, 1], 3), -1
    c3, t3 = ([0, 5, 3, 1], 5), 1
    c4, t4 = ([1, 5, 2], 0), -1

    fn = find_arr_mountain
    assert fn(*c1) == t1
    assert fn(*c2) == t2
    assert fn(*c3) == t3
    assert fn(*c4) == t4

    fn2 = find_arr_mountain_opt
    assert fn2(*c1) == t1
    assert fn2(*c2) == t2
    assert fn2(*c3) == t3
    assert fn2(*c4) == t4
