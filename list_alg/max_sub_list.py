'''
给定一个整数序列，找到最长上升子序列（LIS），返回LIS的长度。
'''


def max_sub_list(nums):
    '''
    动态规划(O)
    dp(i)表示前i个序列中的上升子序列最长长度
    :param nums:
    :return:
    '''
    if nums is None or len(nums) == 0:
        return 0
    result = [1] * len(nums)
    for i in range(len(nums)):
        for k in range(len(result)):
            if nums[i] > nums[k] and (result[k] + 1) > result[i]:
                result[i] = result[k] + 1
    return result[len(nums) - 1]


def max_sub_list_2(nums):
    '''
    动态规划＋二分法（效率最高）
    :param nums:
    :return:
    '''
    if nums is None or len(nums) == 0:
        return 0
    result = [nums[0]]
    for i in range(1, len(nums)):
        if nums[i] > result[-1]:
            result.append(nums[i])
        else:
            # 二分查找并替换
            index = BinarySearch(result, 0, len(result) - 1, nums[i])
            result[index] = nums[i]

    return len(result)


def BinarySearch(input_list, start, end, value):
    if input_list[end] <= value:
        return end + 1
    while start < end:
        mid = start + (end - start) // 2
        if input_list[mid] <= value:
            start = mid + 1
        else:
            end = mid
    return start


if __name__ == '__main__':
    arr = [1, 4, 3, 6, 9, 8, 7]
    print(max_sub_list(arr))
    print(max_sub_list_2(arr))
