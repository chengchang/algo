# coding: utf-8

# from: https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/
# keys: n_sum, ij

from typing import List


# Time: O(n), Space: O(1)
def two_sum_sorted(nums: List[int], target: int) \
        -> List[int]:
    if not nums:
        return []

    i, j = 0, len(nums) - 1
    while i < j:
        cur = nums[i] + nums[j]
        if target == cur:
            return [i + 1, j + 1]
        elif target > cur:
            i += 1
        else:
            j -= 1
    return []


if __name__ == '__main__':
    print(two_sum_sorted([2, 7, 11, 15], 9))
