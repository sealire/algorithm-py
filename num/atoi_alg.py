'''
实现atoi这个函数，将一个字符串转换为整数。如果没有合法的整数，返回0。如果整数超出了32位整数的范围，返回INT_MAX(2147483647)如果是正整数，或者INT_MIN(-2147483648)如果是负整数。
'''


def atoi_a(str):
    if str is None or len(str) == 0:
        return 0
    str = str.strip()
    str = str[0:str.index('.')]
    if len(str) == 0:
        return 0

    index = 0
    sign = 1
    if str[index] == '+' or str[index] == '-':
        index += 1
        sign = -1 if str[0] == '-' else 1

    sum = 0
    for i in range(index, len(str)):
        v = char2num(str[i])
        if v < 0:
            sum = 0
            break
        sum = sum * 10 + v
    return sum * sign


def char2num(c):
    switch = {
        "0": lambda x: 0,
        "1": lambda x: 1,
        "2": lambda x: 2,
        "3": lambda x: 3,
        "4": lambda x: 4,
        "5": lambda x: 5,
        "6": lambda x: 6,
        "7": lambda x: 7,
        "8": lambda x: 8,
        "9": lambda x: 9
    }

    try:
        return switch[c](c)
    except KeyError as e:
        return -1


if __name__ == '__main__':
    print(atoi_a(" -88.32.1  "))
