def linear_search(arr, target):
    for i, v in enumerate(arr):
        if v == target:
            return i
    return -1


def binary_search_recursive(arr, l, r, target):
    if l > r:
        return -1
    m = (l + r) // 2
    if arr[m] == target:
        return m
    if target > arr[m]:
        return binary_search_recursive(arr, m + 1, r, target)
    return binary_search_recursive(arr, l, m - 1, target)


def binary_search_iterative(arr, l, r, target):
    while l <= r:
        m = (l + r) // 2
        if arr[m] == target:
            return m
        if target > arr[m]:
            l = m + 1
        else:
            r = m - 1
    return -1


if __name__ == '__main__':
    arr = [1, 3, 5, 8, 23, 123, 234, 456, 734, 1000]
    tests = [[8, 2], [234, 5], [1000, -1]]
    for target, result in tests:
        assert binary_search_iterative(arr, 0, len(arr) - 1, target) == result


