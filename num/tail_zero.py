# -*- coding:utf-8 -*-
import math


def zero(n):
    '''
    计算出n阶乘中尾部零的个数

    2 * 5 会产生一个0，所以要计算这些数里有几个5
    ret = n / 5 + n / 5^2 + n / 5^3 + ⋯
    '''

    x = math.floor(math.log(n, 5))

    s = 0
    while x > 0:
        s += n // (5 ** x)
        x = x - 1

    return s


if __name__ == '__main__':
    print(math.factorial(26))
    print(zero(26))
