'''
给定一个字符串和一个偏移量，根据偏移量旋转字符串，正向旋转，反向旋转
'''


def rotate(str, count, forward=True):
    arr = [k for k in str]
    temp = [''] * count
    length = len(str)

    if forward:
        temp = [arr[k] for k in range(length - count, length)]

        for k in range(length - count)[::-1]:
            arr[k + count] = arr[k]
        for k in range(count):
            arr[k] = temp[k]
    else:
        temp = [arr[k] for k in range(count)]
        for k in range(length - count):
            arr[k] = arr[k + count]
        for k in range(count):
            arr[k + length - count] = temp[k]

    return ''.join(arr)


if __name__ == '__main__':
    print(rotate("abcdefg", 2, forward=False))
