# coding: utf-8

# from: https://leetcode-cn.com/problems/longest-increasing-subsequence/
# keys: dp, binary_search

from typing import List


def inc_sub_seq_len_dp(nums: List[int]) \
        -> int:
    # 特判
    if not nums:
        return 0

    n = len(nums)

    # d[i] 最长子序列长度
    d = [0] * n
    # 最大值
    m = 1

    # 10, 9, 2, 5, 3, 7, 101, 18
    #           i ->
    #  j -> i
    # d[i] = max(d[i], j_len)
    d[0] = 1
    for i in range(1, n):
        for j in range(i):
            cur = 1
            if nums[i] > nums[j]:
                # new_i > len_j, len++
                cur = d[j] + 1
            d[i] = max(d[i], cur)
        m = max(m, d[i])
    print(m)
    return m


def bs_insert(arr: List[int],
              key: int) -> int:
    left, right = 0, len(arr)
    while left < right:
        # 左中值
        mid = (left + right) // 2
        # 1 3 5 7
        # mid=2, val=5
        if arr[mid] < key:
            #  5 < 6
            left = mid + 1
        else:
            #  5 > 3
            #  5 = 5
            right = mid
    return left


def inc_sub_seq_len_dp_bs(nums: List[int]) \
        -> int:
    # 特判
    if not nums:
        return 0

    n = len(nums)

    # d[i] 为 i + 1 结尾最小数字
    # new_i > d[i]
    d = [nums[0]]
    for i in range(1, n):
        cur = nums[i]
        pos = bs_insert(d, cur)
        if pos == len(d):
            d.append(cur)
        else:
            d[pos] = cur
    return len(d)


if __name__ == '__main__':
    assert bs_insert([1, 3, 5, 7], 5) == 2
    assert bs_insert([1, 3, 5, 7], 4) == 2
    assert bs_insert([1, 3, 5, 7], 8) == 4

    case, true = [10, 9, 2, 5, 3, 7, 101, 18], 4
    assert inc_sub_seq_len_dp(case) == true
    assert inc_sub_seq_len_dp_bs(case) == true
