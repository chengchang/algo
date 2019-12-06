# coding: utf-8
# from: https://leetcode-cn.com/problems/median-of-two-sorted-arrays/
# keys: binary_search

from typing import List


def find_median(nums1: List[int],
                nums2: List[int]) -> float:
    total = len(nums1) + len(nums2)
    half = total // 2
    if total & 1 == 1:
        return _get_kth(nums1, nums2, half + 1)
    x = _get_kth(nums1, nums2, half)
    y = _get_kth(nums1, nums2, half + 1)
    return (x + y) / 2


def _get_kth(nums1: List[int],
             nums2: List[int], k: int) -> float:
    n1, n2 = len(nums1), len(nums2)
    b1, b2 = 0, 0
    while True:
        # 长度为空的数组，返回对方第 k项，b为偏移
        if n1 == 0:
            return nums2[b2 + k - 1]
        if n2 == 0:
            return nums1[b1 + k - 1]

        # k 为 1 时说明已经排除完成，返回较小的那个
        if k == 1:
            return min(nums1[b1], nums2[b2])

        # 本轮
        # 1 3 6 8
        # 2 5 6 9
        # 1 2 3 5 6 6 8 9

        # 折半
        i = min(k // 2, n1)
        j = min(k - i, n2)

        # 当前最小
        x = nums1[b1 + i - 1]
        y = nums2[b2 + j - 1]

        # 相等直接找到
        if i + j == k and x == y:
            return x

        # 1 大，2缩小范围
        if x >= y:
            b2 += j
            n2 -= j
            k -= j

        # 2 大，1缩小范围
        if x <= y:
            b1 += i
            n1 -= i
            k -= i


if __name__ == '__main__':
    # print(find_median_sorted_arrays([1, 3], [2]))
    assert find_median([1, 2], [3, 4]) == 2.5
