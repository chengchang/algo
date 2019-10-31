# coding: utf-8

# from: https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/
# keys: binary_search


from typing import List


def find_min(nums: List[int]) -> int:
    if not nums:
        raise ValueError('bad params')

    # 边界
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) >> 1
        # 4, 5, 6, 7, 0, 1, 2
        # l=0      m=3      r=6  -> b1 l=3
        #          l=3      r=6  -> b2 r=4
        #          lm r          -> b1 l=4

        # 找升序变化点
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            # assert nums[mid] < nums[right]
            # 无重复元素，无=
            right = mid

    return nums[left]


if __name__ == '__main__':
    case1, true1 = [3, 4, 5, 1, 2], 1
    case2, true2 = [4, 5, 6, 7, 0, 1, 2], 0
    assert find_min(case1) == true1
    assert find_min(case2) == true2
