def max_comm_list(str1, str2):
    '''
    给出两个字符串，找到最长公共子序列(LCS)，返回LCS的长度。

    动态规划:
        确定状态：
        最后一步：观察A[m-1]和B[n-1]这两个字符是否作为一个对子在最优策略中
        状态：设f[i][j]为A前i个字符A[0..i-1]和B前j个字符[0..j-1]的最长公共子序列的长度
        转移方程：f[i][j] = max{f[i-1][j], f[i][j-1], f[i-1][j-1]+1|A[i-1]=B[j-1]}
        初始条件和边界情况：
        f[0][j] = 0, j=0..n
        f[i][0] = 0, i=0..m
        计算顺序：
        f[0][0..n-1]
        …
        f[m-1][0..n-1]
        答案是f[m][n]
    :param str1:
    :param str2:
    :return:
    '''
    length1 = len(str1)
    length2 = len(str2)
    if length1 == 0 or length2 == 0:
        return -1
    c = [[0 for _ in range(length1 + 1)] for _ in range(length2 + 1)]
    for i in range(1, length2 + 1):
        for j in range(1, length1 + 1):
            if str2[i - 1] == str1[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
            else:
                c[i][j] = max(c[i][j - 1], c[i - 1][j])
    return c[-1][-1]


def max_comm_str(s1, s2):
    m = [[0 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]  # 生成0矩阵，为方便后续计算，比字符串长度多了一列
    mmax = 0  # 最长匹配的长度
    p = 0  # 最长匹配对应在s1中的最后一位
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                m[i + 1][j + 1] = m[i][j] + 1
            if m[i + 1][j + 1] > mmax:
                mmax = m[i + 1][j + 1]
                p = i + 1
    return s1[p - mmax:p], mmax  # 返回最长子串及其长度


if __name__ == '__main__':
    print(max_comm_list('abcde', 'afcdg'))
    print(max_comm_str('fasdfasasdfasdfdsafadfasdfa', 'fasfadsafddfdfas'))
