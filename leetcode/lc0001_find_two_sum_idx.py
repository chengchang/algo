# coding: utf-8

# from: https://leetcode-cn.com/problems/two-sum/
# keys: n_sum, idx_cache

from typing import List


# Time: O(n^2), Space: O(1)
def two_sum(nums: List[int],
            target: int) -> List[int]:
    if not nums:
        return []

    n = len(nums)
    for i in range(n):
        for j in range(n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


# Time: O(n), Space: O(n)
def two_sum_cached(nums: List[int],
                   target: int) -> List[int]:
    if not nums:
        return []

    n = len(nums)
    idx_cache = dict()  # pre -> idx
    for i in range(n):
        cur = nums[i]
        pre = target - cur
        if pre in idx_cache:
            return [idx_cache[pre], i]
        else:
            idx_cache[cur] = i
    return []


if __name__ == '__main__':
    fn1, fn2 = two_sum, two_sum_cached
    assert fn1([2, 7, 11, 15], 9) == [0, 1]
    assert fn2([2, 7, 11, 15], 9) == [0, 1]
