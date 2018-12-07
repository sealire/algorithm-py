'''
两个排序的数组A和B分别含有m和n个数，找到两个排序数组的中位数，要求时间复杂度应为O(log (m+n))。
'''


def median(list1, list2):
    ''
    if len(list1) == 0:
        return list2[len(list2) // 2]
    if len(list2) == 0:
        return list1[len(list1) // 2]


if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5, 6, 76, 78]
    list2 = [4, 5, 6, 7, 89, 98]

    print(median(list1, list2))
