# coding: utf-8

# from: https://leetcode-cn.com/problems/3sum-closest/
# keys: n_sum, ij


from typing import List


# Time: O(n^3), Space: O(1)
def three_sum_closest(arr: List[int],
                      target: int) -> int:
    dis, ret = float('inf'), 0

    k = len(arr) - 1
    while k >= 2:
        j = k - 1
        while j >= 1:
            for i in range(j):
                cur = arr[i] + arr[j] + arr[k]
                cur_dis = abs(cur - target)
                if cur_dis == 0:
                    return cur

                if cur_dis < dis:
                    dis = cur_dis
                    ret = cur
            j -= 1
        k -= 1
    return ret


# Time: O(n^2), Space: O(1)
def three_sum_closest_ij(arr: List[int],
                         target: int) -> int:
    # -1, 2, 1, -4
    arr.sort()  # Time: n*log(n)

    # -4, -1, 1, 2
    #         <- k
    # i ->
    #      <- j
    n = len(arr)
    k = n - 1
    dis, ret = float('inf'), 0
    while k >= 2:
        i, j = 0, k - 1
        while i < j:
            cur = arr[i] + arr[j] + arr[k]
            if cur == target:
                return cur
            elif cur < target:
                i += 1
            else:
                j -= 1
            cur_dis = abs(cur - target)
            if dis > cur_dis:
                dis = cur_dis
                ret = cur
        k -= 1

    return ret


if __name__ == '__main__':
    fn1, fn2 = three_sum_closest, three_sum_closest_ij
    assert fn1([-1, 2, 1, -4], 1) == 2
    assert fn2([-1, 2, 1, -4], 1) == 2
