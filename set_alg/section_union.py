from collections import deque

'''
在一个递增实数区间集合中插入一个新区间，合并成新的递增区间
'''


def sec_union(secs, s):
    nsecs = deque()
    nsecs.append(s)

    length = len(secs)
    for i in range(length):
        ss = nsecs.pop()
        sec = secs[i]

        if sec[1] < ss[0]:
            nsecs.append(sec)
            nsecs.append(ss)
        else:
            ml, mr = min(sec[0], ss[0]), max(sec[1], ss[1])
            nsecs.append([ml, mr])
    print(nsecs)
    return nsecs


if __name__ == '__main__':
    secs = [[1, 2], [6, 7], [8, 10]]
    sec_union(secs, [4, 5])
