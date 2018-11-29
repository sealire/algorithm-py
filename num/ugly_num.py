# -*- coding:utf-8 -*-

def ugly(n):
    '''
    计算第n个丑数，丑数是只含有2，3，5质因子的数

    1，2，3，4，5，……
    '''
    ug = [0] * n

    for x in range(5):
        ug[x] = x + 1

    i2 = i3 = i5 = 0
    last = 5
    while last < n:
        n2 = ug[i2] * 2
        n3 = ug[i3] * 3
        n5 = ug[i3] * 5
        ns = [n2, n3, n5]
        m = min(ns)

        if m > ug[last - 1]:
            ug[last] = m
            last = last + 1

        min_index = ns.index(m)
        if min_index == 0:
            i2 = i2 + 1
        elif min_index == 1:
            i3 = i3 + 1
        else:
            i5 = i5 + 1
    print(ug)
    return ug[n - 1]


if __name__ == '__main__':
    print(ugly(18))
