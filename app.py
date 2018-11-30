from collections import deque


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


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(BinarySearch(arr, 9, 9))
