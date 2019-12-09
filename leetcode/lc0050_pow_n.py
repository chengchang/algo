# coding: utf-8
# from: https://leetcode-cn.com/problems/powx-n
# keys: bit


def pow_n(x: float, n:int) -> float:
    if n == 0:
        return 1.0

    if n < 0:
        x = 1 / x
        n = abs(n)

    res = 1.0
    while n != 0:
        if n & 1 == 1:
            res *= x
        x *= x
        n //= 2

    return res


if __name__ == '__main__':
    assert pow_n(2.0, 10) == 1024.0
    assert pow_n(2.0, -1) == 0.5
