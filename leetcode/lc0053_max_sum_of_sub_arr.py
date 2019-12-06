# coding: utf-8
# from: https://leetcode-cn.com/problems/maximum-subarray/
# keys: greedy

from typing import List


def max_sum_sub_arr(nums: List[int]) -> int:
    ans = nums[0]
    cur = 0

    for n in nums:
        cur += n
        ans = max(ans, cur)
        if cur < 0:
            cur = 0

    return ans


if __name__ == '__main__':
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert max_sum_sub_arr(arr) == 6
