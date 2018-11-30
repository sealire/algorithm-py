'''
给出三个字符串:s1、s2、s3，判断s3是否由s1和s2交叉构成

使用动态规划计算s3是从s1还是s2添加字符的
'''


def interv(s1, s2, s3):
    ls1 = len(s1)
    ls2 = len(s2)
    ls3 = len(s3)

    if ls3 != ls1 + ls2:
        return False

    dp = [[]] * (ls1 + 1)
    for i in range(ls1 + 1):
        dp[i] = [False] * (ls2 + 1)

    dp[0][0] = True
    for i in range(0, ls2):
        if s2[i] == s3[i] and dp[0][i]:
            dp[0][i + 1] = True

    for i in range(0, ls1):
        if s1[i] == s3[i] and dp[i][0]:
            dp[i + 1][0] = True

    for si in range(1, ls1 + 1):
        for sk in range(1, ls2 + 1):
            if (s3[si + sk - 1] == s2[sk - 1] and dp[si][sk - 1]) or (s3[si + sk - 1] == s1[si - 1] and dp[si - 1][sk]):
                dp[si][sk] = True

    print(dp)
    return dp[ls1][ls2]


if __name__ == '__main__':
    s1 = "abcedfg"
    s2 = "hijklm"
    s3 = "abhicejkdlfmg"

    print(interv(s1, s2, s3))
