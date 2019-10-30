# coding: utf-8


# from: https://leetcode-cn.com/problems/4sum/
# keys: n_sum, ij

from typing import List


# Time: O(n^4), Space: O(1)
def four_sum(nums: List[int], target: int) \
        -> List[List[int]]:
    if not nums:
        return []

    ret = []
    p = len(nums) - 1
    while p >= 3:
        k = p - 1
        while k >= 2:
            j = k - 1
            while j >= 1:
                for i in range(j):
                    cur = [nums[i], nums[j],
                           nums[k], nums[p]]
                    if target == sum(cur):
                        ret.append(cur)
                j -= 1
            k -= 1
        p -= 1

    return ret


# Time: O(n^3), Space: O(1)
def four_sum_ij(nums: List[int], target: int) \
        -> List[List[int]]:
    if not nums:
        return []

    nums.sort()

    ret = []
    p = len(nums) - 1
    while p >= 3:
        new_t = target - nums[p]
        k = p - 1
        while k >= 2:
            i, j = 0, k - 1
            nk = nums[k]
            while i < j:
                ni, nj = nums[i], nums[j]
                cur = ni + nj + nk
                if new_t == cur:
                    ret.append([nums[p], nk, nj, ni])
                    while i < j and nums[i + 1] == ni:
                        i += 1
                    while i < j and nums[j - 1] == nj:
                        j -= 1
                    i += 1
                    j -= 1
                elif new_t > cur:
                    i += 1
                else:
                    j -= 1
            while k >= 2 and nums[k - 1] == nums[k]:
                k -= 1
            k -= 1

        while p >= 2 and nums[p - 1] == nums[p]:
            p -= 1
        p -= 1

    return ret


if __name__ == '__main__':
    print(four_sum([1, 0, -1, 0, -2, 2], 0))
    print(four_sum_ij([1, 0, -1, 0, -2, 2], 0))
