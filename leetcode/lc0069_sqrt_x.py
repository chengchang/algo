# coding: utf-8

# from: https://leetcode-cn.com/problems/sqrtx/
# keys: binary_search


def sqrt_x(x: int) -> int:
    if x < 0:
        raise ValueError('bad x=%d (< 0)' % x)

    low, high = 0, x
    while low <= high:
        mid = low + (high - low) // 2
        val = mid * mid
        if val == x:
            return mid
        elif x > val:
            low = mid + 1
        else:
            high = mid - 1

    # always high
    return high


def sqrt_x_better(x: int) -> int:
    if x < 0:
        raise ValueError('bad x=%d (< 0)' % x)

    # 上下界
    left, right = 0, x // 2 + 1

    while left < right:
        # 右中值
        mid = left + (right - left + 1) // 2

        # 右中值不包括 3 * 3 > 7 ?
        if mid * mid > x:
            right = mid - 1
        else:
            # assert mid * mid <= x
            # 2 * 2 <= 4 => =
            # 2 * 2 <= 7 => <
            left = mid
    return left


if __name__ == '__main__':
    assert sqrt_x(4) == 2
    assert sqrt_x(8) == 2
    assert sqrt_x(15) == 3

    assert sqrt_x_better(4) == 2
    assert sqrt_x_better(8) == 2
    assert sqrt_x_better(15) == 3
