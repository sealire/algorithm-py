'''
扔 n 个骰子，向上面的数字之和为 S。给定 Given n，请列出所有可能的 S 值及其相应的概率。

使用动态规划计算 p[i + 1][k + s] = p[i][k] / 6
'''


def dice_prob(n):
    if n < 1:
        return None
    probs = [[]] * (n + 1)
    for i in range(n + 1):
        probs[i] = [0] * (6 * n + 1)

    for i in range(1, 7):
        probs[1][i] = 1 / 6

    for i in range(1, n):
        for k in range(i, (6 * i + 1)):
            if probs[i][k] > 0:
                for s in range(1, 7):
                    probs[i + 1][k + s] += probs[i][k] / 6
    return [[i, probs[n][i]] for i in range(1, 6 * n + 1) if probs[n][i] > 0.0]


if __name__ == '__main__':
    print(dice_prob(3))
