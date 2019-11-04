# coding: utf-8

# from: https://leetcode-cn.com/problems/binary-search/
# keys: binary_search

from typing import List


# Time: O(log(n)), Space: O(1)
def binary_search(nums: List[int], target: int) -> int:
    if not nums:
        return -1

    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2  # avoid overflow
        if target < nums[mid]:
            high = mid - 1
        elif target > nums[mid]:
            low = mid + 1
        else:
            return mid
    return -1


if __name__ == '__main__':
    c1, t1 = ([-1, 0, 3, 5, 9, 12], 9), 4
    c2, t2 = ([-1, 0, 3, 5, 9, 12], 2), -1
    assert binary_search(*c1) == t1
    assert binary_search(*c2) == t2
