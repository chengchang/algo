# coding: utf-8

# from: https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii
# keys: binary_search


from typing import List


def find_min(nums: List[int]) -> int:
    if not nums:
        raise ValueError('bad params')

    # 边界
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) >> 1
        # 2    2    2    0    1
        # l=0       m=2       r=4  -> b1 l=3
        #                l    r=4  -> b2 r=3

        # 2    2    2    0    2
        # l=0       m=2       r=4  -> b3 r=3
        # l=0  m=1       r=3       -> b1 l=2
        #           l    r         -> b1 l=3

        # 找升序变化点
        cur, r_val = nums[mid], nums[right]
        if cur > r_val:
            left = mid + 1
        elif cur < r_val:
            right = mid
        else:
            # assert cur == r_val
            right -= 1

    return nums[left]


if __name__ == '__main__':
    case1, true1 = [3, 4, 5, 1, 2], 1
    case2, true2 = [4, 5, 6, 7, 0, 1, 2], 0
    case3, true3 = [1, 3, 5], 1
    case4, true4 = [2, 2, 2, 0, 1], 0
    case5, true5 = [2, 2, 2, 0, 2], 0
    assert find_min(case1) == true1
    assert find_min(case2) == true2
    assert find_min(case3) == true3
    assert find_min(case4) == true4
    assert find_min(case5) == true5
