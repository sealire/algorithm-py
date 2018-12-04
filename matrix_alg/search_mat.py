'''
写出一个高效的算法来搜索m×n矩阵中的值，返回这个值出现的次数。

这个矩阵具有以下特性：

每行中的整数从左到右是排序的。
每一列的整数从上到下是排序的。
在每一行或每一列中没有重复的整数。
'''


def search(mat, num):
    if mat is None:
        return 0
    count, row, col = 0, len(mat) - 1, 0
    while row >= 0 and col < len(mat[0]):
        if num < mat[row][col]:
            row -= 1
        elif num > mat[row][col]:
            col += 1
        else:
            count += 1
            row -= 1
            col += 1

    return count


if __name__ == '__main__':
    mat = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
    print(mat)
    print(search(mat, 5))
