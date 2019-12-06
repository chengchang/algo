# coding: utf-8
# from: https://leetcode-cn.com/problems/majority-element/
# keys: moore-vote

from typing import List


def majority_num(nums: List[int]) -> int:
    cur = nums[0]
    cnt = 0

    for n in nums:
        if cur == n:
            cnt += 1
        else:
            cnt -= 1
            if cnt == 0:
                cur = n
                cnt = 1
    return cur


if __name__ == '__main__':
    arr1 = [3, 2, 3]
    assert majority_num(arr1) == 3
    arr2 = [2, 2, 1, 1, 1, 2, 2]
    assert majority_num(arr2) == 2
