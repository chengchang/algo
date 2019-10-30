# coding: utf-8

# from: https://leetcode-cn.com/problems/3sum/
# keys: n_sum, ij

from typing import List


# Time: O(n^2), Space: O(1)
def three_sum_ij(nums: List[int]) -> List[List[int]]:
    if not nums:
        return []

    nums.sort()

    ret = []
    k = len(nums) - 1
    while k >= 2:
        if nums[k] < 0:   # early stop if third < 0
            break

        i, j = 0, k - 1
        while i < j:
            cur = nums[i] + nums[j] + nums[k]
            if cur == 0:
                ret.append([nums[i], nums[j], nums[k]])
                while i < j and nums[i + 1] == nums[i]:
                    i += 1
                while i < j and nums[j - 1] == nums[j]:
                    j -= 1
                i += 1
                j -= 1
            elif cur > 0:
                j -= 1
            else:
                i += 1

        while k >= 2 and nums[k - 1] == nums[k]:  # move
            k -= 1
        k -= 1
    return ret


if __name__ == '__main__':
    print(three_sum_ij([-1, 0, 1, 2, -1, -4]))
