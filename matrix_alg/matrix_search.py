'''
写出一个高效的算法来搜索 m × n矩阵中的值。

这个矩阵具有以下特性：

每行中的整数从左到右是排序的。
每行的第一个数大于上一行的最后一个整数。

用两次二分查找
'''


def FirstLeast(input_list, end, value):
    if value < input_list[0]:
        return -1

    left = 0
    right = end - 1
    while left <= right:
        middle = left + (right - left) // 2
        if input_list[middle] > value:
            right = middle - 1
        else:
            left = middle + 1

    return left - 1


def BinarySearch(input_list, end, value):
    left = 0
    right = end - 1
    while left <= right:
        middle = left + (right - left) // 2
        if input_list[middle] >= value:
            right = middle - 1
        else:
            left = middle + 1

    return left if left < end else -1


def mat_search(mat, num):
    lsi = len(mat)
    s0 = [mat[i][0] for i in range(lsi)]

    mid = FirstLeast(s0, lsi, num)
    if mid < 0:
        return False

    sk = BinarySearch(mat[mid], len(mat[mid]), num)
    if sk >= 0:
        return [mid, sk]
    else:
        return False


if __name__ == '__main__':
    mat = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]

    print(mat_search(mat, 11))
