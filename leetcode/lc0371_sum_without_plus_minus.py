# coding: utf-8
# from: https://leetcode-cn.com/problems/sum-of-two-integers
# keys: bit


def bit_opt_sum(a: int, b: int) -> int:
    MASK = 0xFFFFFFFF
    MAX_INT = 0x7FFFFFFF
    # pos: 0 ~ 0x7FFFFFFF
    # neg: 0x80000000 ~ 0xFFFFFFFF

    while b != 0:
        sum_ = (a ^ b) & MASK
        carry = ((a & b) << 1) & MASK
        a = sum_
        b = carry

    # ~ = -x-1
    return a if a <= MAX_INT else ~(a ^ MASK)


if __name__ == '__main__':
    assert bit_opt_sum(9, 11) == 20
    assert bit_opt_sum(-5, 3) == -2
