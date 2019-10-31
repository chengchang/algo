# coding: utf-8


# from: https://leetcode-cn.com/problems/find-the-duplicate-number/
# keys: binary_search


from typing import List


def find_dup_num(nums: List[int]) -> int:
    if not nums:
        raise ValueError('bad params')

    left, right = 1, len(nums) - 1
    while left < right:
        mid = left + (right - left + 1) // 2

        # 1, 3, 4, 2, 2  dup=2
        # 1  2  3  4  5
        # l     m     r  m=3, c=3 => b1 r=2
        # l  r           m=2, c=1 => b2 l=2

        # 1, 3, 4, 4, 2  dup=4
        # 1  2  3  4  5
        # l     m     r  m=3, c=2 => b2 l=3
        #       l  m  r  m=4, c=3 => b2 l=4
        #          l  mr m=5, c=5 => b1 r=4

        cnt = 0
        for num in nums:
            if num < mid:
                cnt += 1

        if cnt >= mid:
            right = mid - 1
        else:
            left = mid

    return left


if __name__ == '__main__':
    fn = find_dup_num
    assert fn([1, 3, 4, 2, 2]) == 2
    assert fn([3, 1, 3, 4, 2]) == 3
