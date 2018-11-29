# -*- coding:utf-8 -*-

def num_count(n, k):
    '''
    计算数字k在0到n中的出现的次数，k可能是0~9的一个值

    可以从个位数，十位数，百位数总结规律

    设数字n = Xi+1 Xi Xi-1
    则Xi位上有k的个数规律如下：

        若Xi > k    个数为：(Xi+1 + 1) * 10 ^ i
        若Xi == k   个数为：Xi+1 * 10 ^ i + (Xi-1 + 1)
        若Xi < k    个数为：Xi+1 * 10 ^ i

    另若k == 0，计算方法不一样
        若Xi > 0    个数为：Xi+1 * 10 ^ i
        若Xi == 0   个数为：(Xi+1 - 1) * 10 ^ i + (Xi-1 + 1)
        最后返回结果时+1，第一个0
    '''

    def digits(n):
        '''
        计算数字n的位数
        '''
        if n == 0:
            return 1
        d, r = 0, 10
        while n > 0:
            d += 1
            n //= r
        return d

    def max_x(n, x):
        '''
        计算数字n高x位的数字
        '''
        return n // (10 ** (x + 1))

    def min_x(n, x):
        '''
        计算数字n低x位的数字
        '''
        if x == 0:
            return 0
        return n % (10 ** x)

    def num_x(n, x):
        '''
        计算数字n的x位的数字
        '''
        return (n // (10 ** x)) % 10

    d = digits(n)

    s_k = 0
    for i in range(d):
        max_xi = max_x(n, i)
        xi = num_x(n, i)
        min_xi = min_x(n, i)
        if xi > k:
            if k == 0:
                s_k += max_xi * (10 ** i)
            else:
                s_k += (max_xi + 1) * (10 ** i)
        elif xi == k:
            if k == 0:
                s_k += (max_xi - 1) * (10 ** i) + min_xi + 1
            else:
                s_k += max_xi * (10 ** i) + min_xi + 1
        else:
            s_k += max_xi * (10 ** i)
    return s_k + 1 if k == 0 else s_k


if __name__ == '__main__':
    print(num_count(1001, 1))
