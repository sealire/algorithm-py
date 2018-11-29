# -*- coding:utf-8 -*-

def max_k(input_list, k):
    '''
    在数组中找到第k大的元素

    大根堆排序，查找第k大的元素
    '''
    def HeadAdjust(input_list, parent, length):
        '''
        函数说明:堆调整，调整为最大堆
        Parameters:
            input_list - 待排序列表
            parent - 堆的父结点
            length - 数组长度
        Returns:
            无
        '''
        temp = input_list[parent]
        child = 2 * parent + 1

        while child < length:
            if child + 1 < length and input_list[child] < input_list[child + 1]:
                child += 1
            if temp >= input_list[child]:
                break

            input_list[parent] = input_list[child]

            parent = child
            child = 2 * parent + 1
        input_list[parent] = temp

    if len(input_list) == 0:
        return []
    sorted_list = input_list
    length = len(sorted_list)

    for i in range(0, length // 2)[::-1]:
        HeadAdjust(sorted_list, i, length)

    for j in range(length - k, length)[::-1]:
        temp = sorted_list[j]
        sorted_list[j] = sorted_list[0]
        sorted_list[0] = temp

        HeadAdjust(sorted_list, 0, j)
        print('第%d趟排序:' % (length - j), end='')
        print(sorted_list)
    return sorted_list[length - k]


if __name__ == '__main__':
    input_list = [6, 4, 8, 9, 2, 3, 1]
    print(max_k(input_list, 3))
