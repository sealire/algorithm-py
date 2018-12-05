def two_sum(list_input, target):
    '''
    给一个整数数组，找到两个数使得他们的和等于一个给定的数 target。
    :param list_input:
    :param target:
    :return:
    '''
    dict = {}

    for i in range(len(list_input)):
        dict[str(target - list_input[i])] = i

    for i in range(len(list_input)):
        if dict.get(str(list_input[i])) is not None:
            return (i, dict.get(str(list_input[i])))
    return (-1, -1)


def three_sum(list_input, target):
    ''


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7]
    print(two_sum(arr, 13))
