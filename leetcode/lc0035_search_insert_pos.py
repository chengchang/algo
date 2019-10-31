# coding: utf-8


from typing import List


# Time: O(log(n)), Space: O(1)
def search_insert_pos(arr: List[int],
                      target: int) -> int:
    if not arr:
        return -1

    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        cur = arr[mid]

        if target == cur:
            return mid
        elif target > cur:
            low = mid + 1
        else:
            high = mid - 1

    # always low for insert pos
    return low


def search_insert_pos2(nums: List[int],
                       target: int) -> int:
    n = len(nums)

    # 特判
    if n == 0:
        return 0

    # 定边界，n 可作为位置
    low, high = 0, n

    while low < high:
        # 左中值
        mid = low + (high - low) // 2

        # 1 3 7 10
        #      9    mid=2, val=7 < 9
        if nums[mid] < target:
            # 无中值：mid=3
            low = mid + 1
        else:
            # key = 7 => =
            # key = 6 => >
            # assert arr[mid] >= target
            high = mid

    return low


if __name__ == '__main__':
    fn1 = search_insert_pos
    fn2 = search_insert_pos2
    assert fn1([1, 3, 5, 6], 5) == 2
    assert fn1([1, 3, 5, 6], 4) == 2
    assert fn1([1, 3, 5, 6], 2) == 1
    assert fn1([1, 3, 5, 6], 7) == 4
    assert fn1([1, 3, 5, 6], 0) == 0

    assert fn2([1, 3, 5, 6], 5) == 2
    assert fn2([1, 3, 5, 6], 4) == 2
    assert fn2([1, 3, 5, 6], 2) == 1
    assert fn2([1, 3, 5, 6], 7) == 4
    assert fn2([1, 3, 5, 6], 0) == 0
