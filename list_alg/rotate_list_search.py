'''
假设有一个排序的按未知的旋转轴旋转的数组(比如，0 1 2 4 5 6 7 可能成为4 5 6 7 0 1 2)。给定一个目标值进行搜索，如果在数组中找到目标值返回数组中的索引位置，否则返回-1。
'''


def search(input_list, target):
    if input_list is None or len(input_list) == 0:
        return -1
    begin, end = 0, len(input_list) - 1
    while begin <= end:
        mid = begin + (end - begin) // 2
        if input_list[mid] == target:
            return mid
        if input_list[mid] > input_list[begin]:
            # 此时begin和mid肯定处在同一个递增数组上
            # 那么就直接运用原始的二分查找
            if input_list[begin] <= target and target < input_list[mid]:
                end = mid - 1
            else:
                begin = mid + 1
        else:
            # 此时mid处于第二个递增数组
            # begin处于第一个递增数组
            # 自然的mid和end肯定处于第二个递增数组上
            # 还是直接运用原始的二分查找思想
            if input_list[mid] < target and target <= input_list[end]:
                begin = mid + 1
            else:
                end = mid - 1
    return -1


if __name__ == '__main__':
    li = [5, 6, 7, 8, 1, 2, 3, 4]
    print(search(li, 4))
