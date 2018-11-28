# -*- coding:utf-8 -*-

def insertSort(input_list):
    '''
    函数说明:插入排序（升序）
    Parameters:
        input_list - 待排序列表
    Returns:
        sorted_list - 升序排序好的列表
    '''
    if len(input_list) == 0:
        return []
    sorted_list = input_list

    for i in range(1, len(sorted_list)):
        temp = sorted_list[i]
        j = i - 1
        while j >= 0 and temp < sorted_list[j]:
            sorted_list[j + 1] = sorted_list[j]
            j -= 1
        sorted_list[j + 1] = temp
    return sorted_list


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


def BinaryInsertSort(input_list):
    '''
    函数说明:二分插入排序（升序）
    Parameters:
        input_list - 待排序列表
    Returns:
        sorted_list - 升序排序好的列表
    '''
    if len(input_list) == 0:
        return []
    result = input_list
    for i in range(1, len(input_list)):
        j = i - 1
        temp = result[i]
        insert_index = BinarySearch(result, i, result[i])
        if insert_index != -1:
            while j >= insert_index:
                result[j + 1] = result[j]
                j -= 1
            result[j + 1] = temp
    return result


if __name__ == '__main__':
    input_list = [6, 4, 8, 9, 2, 3, 4, 1]
    print('排序前:', input_list)
    sorted_list = BinaryInsertSort(input_list)
    print('排序后:', sorted_list)
